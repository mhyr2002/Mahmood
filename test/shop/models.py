from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=255)
    slug= models.SlugField(max_length=255,unique=True)

    class Meta :
        ordering = ['name',]

        indexes = [
            models.Index(fields=['name',])
        ]

        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_absolute_urls(self):
        return reverse('shop:products_list_by_category', args=[self.slug,])

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE,verbose_name='category')
    name = models.CharField(max_length=255,verbose_name='name')
    slug = models.SlugField(max_length=255,verbose_name='slug')
    description = models.TextField(max_length=1200,verbose_name='description')
    inventory = models.PositiveIntegerField(default=0 , verbose_name='inventory')
    price = models.PositiveIntegerField(default=0, verbose_name='price')
    off = models.PositiveIntegerField(default=0,verbose_name='off')
    new_price = models.PositiveIntegerField(default=0,verbose_name='new_price')
    created = models.DateTimeField(auto_now_add=True,verbose_name='create time')
    updated =  models.DateTimeField(auto_now=True,verbose_name='updated time')

    class Meta:
        ordering=['-created']
        indexes=[
            models.Index(fields=['id','slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
    
        ]

    def get_absolute_urls(self):
        return reverse('shop:product_detail', args=[self.id,self.slug])

    def __str__(self):
        return self.name
    
class Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images',verbose_name='product')
    file = models.ImageField(upload_to="product_images/%Y/%m/%d")
    title =models.CharField(max_length=255,verbose_name='tilte',null=True,blank=True)
    description = models.TextField(verbose_name='descripton',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='created')

    class Meta:
        ordering=['-created']
        indexes=[
            models.Index(fields=['-created'])
        ]

        verbose_name= 'picture'
        verbose_name_plural = 'pictures' 

class ProductFeatures(models.Model):
    name= models.CharField(max_length=255, verbose_name='feature name')
    value = models.CharField(max_length=255, verbose_name='quantity of feature')
    product = models.ForeignKey(Product,related_name='features',on_delete=models.CASCADE,verbose_name='product')

    def __str__(self):
        return f'{self.name} : {self.value}'