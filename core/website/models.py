from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=225)
    email=models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return "{}  {}".format(self.name, self.email)

class NewsLetter (models.Model):
    email = models.EmailField()

    def __str__(self) :
        return self.email