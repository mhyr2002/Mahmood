from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django.template.defaultfilters import truncatechars
from taggit.managers import TaggableManager

class Category (models.Model):
    name = models.CharField(max_length=225)

    def __str__ (self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    truncated_content = models.TextField(null=True)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category =models.ManyToManyField(Category)
    tags = TaggableManager()
    counted_view = models.IntegerField(default = 0)
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    admin_selected = models.BooleanField(default=False,blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    class Meta:
        ordering = ['created_date']
        #verbos_name 
        #verbos_name_plural 
    def __str__(self) :
        return "{} | {}".format(self.id,self.title)
    
    def get_absolute_url (self):
        return reverse ('blog:single',kwargs={'pid':self.id})
    
class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message= models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self) :
        return self.name + " " + self.email