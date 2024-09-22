from django.contrib import admin
from website.models import Contact,NewsLetter
# Register your models here.


class AdminContact(admin.ModelAdmin):

    date_hireachy = "created_date"
    list_display = ("name", "email", "created_date")
    list_filter = ("email",)
    search_fields = ["name", "message"]


admin.site.register(Contact, AdminContact)
admin.site.register(NewsLetter )