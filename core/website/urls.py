from django.urls import path
from .views import *


app_name='website'
#setare baes mishe ke tamami tavabe mojod dar in calss import she
urlpatterns = [
    path('',home,name='home'),
    path('about',about_view,name= 'about'),
    path('contact',contact_view,name= 'contact'),
    path('newsletter',newsletter_view,name= 'newsletter'),
    # path('test',test,name= 'test'),
    
]

