from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # ایمپورت فرم سفارشی
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            form = AuthenticationForm()
        
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')



def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)  # استفاده از فرم سفارشی
            if form.is_valid():
                user = form.save()
                login(request, user)  # احراز هویت و لاگین کاربر تازه ثبت‌نام شده
                return redirect('/')
        else:
            form = CustomUserCreationForm()  # استفاده از فرم سفارشی
        
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')


# View for requesting password reset
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            email = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password_reset_email.html"
                    # اضافه کردن user به context
                    c = {
                        "email": user.email,
                        'domain': get_current_site(request).domain,
                        'site_name': 'Your Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                        'protocol': 'http',
                        'user': user,  # اضافه کردن user به context
                    }
                    email_content = render_to_string(email_template_name, c)
                    send_mail(subject, email_content, 'admin@yourdomain.com', [user.email], fail_silently=False)
                messages.success(request, 'A reset link has been sent to your email address.')
            else:
                messages.error(request, 'No user is associated with this email address.')
            return redirect('accounts:password_reset_request')
    else:
        password_reset_form = PasswordResetForm()
    return render(request, 'accounts/password_reset_request.html', {'form': password_reset_form})



# View for confirming the password reset
def password_reset_confirm(request, uidb64=None, token=None):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password has been reset successfully.')
                return redirect('accounts:login')
        else:
            form = SetPasswordForm(user)
        return render(request, 'accounts/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, 'The reset link is invalid, possibly because it has already been used.')
        return redirect('accounts:password_reset_request')