from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from website.forms import ContactForm,NewsLetterForm
from django.contrib import messages
from blog.models import Post,Comment
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.SUCCESS,'your ticket didn t sumbite')
    form = ContactForm()
    posts_popular =Post.objects.filter(status=1).order_by('-counted_view')[0:4]
    post_first = posts_popular[0]
    post_second = posts_popular[1]
    post_third = posts_popular[2]
    post_fourth =posts_popular[3]

    context = {
        'form': form,
        'post_first': post_first,
        'post_second': post_second,
        'post_third': post_third,
        'post_fourth': post_fourth,
    }
    return render(request,'website/home.html',context)

def about_view(request):
    return render(request,'website/about-us.html')

def contact_view(request):
    return render(request,'website/contact-us.html')



""" funcions for receiving form from newsletter"""
def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else :
        return HttpResponseRedirect('/')