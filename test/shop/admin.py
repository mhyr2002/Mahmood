from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    #besorat khud kar field slug ra barasas name por konad 
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'off', 'created', 'updated','inventory')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created', 'updated')

    #dar zir khud mahsul aks ha va fearure hara namayesh dahad 
    class FeatureInLine(admin.TabularInline): 
        model = ProductFeatures
        extra = 0

    class ImageInLine(admin.TabularInline):
        model = Image
        extra = 0

    


