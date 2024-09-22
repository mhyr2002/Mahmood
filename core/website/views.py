from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from website.forms import ContactForm,NewsLetterForm
from django.contrib import messages
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
    return render(request,'website/home.html',{'form':form})

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