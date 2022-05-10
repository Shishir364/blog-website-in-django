from django.contrib import admin
from .models import Posts,Contacts

class PostRegister(admin.ModelAdmin):
    list_display = ["title","slug","date","sub_title"]
    search_fields=["title","slug"]
    ordering = ["date"]
    list_filter =["title"]


class ContactRegister(admin.ModelAdmin):
    list_display = ["name","email","date","phone_num"]
    search_fields=["name","phone_num"]
    ordering = ["date"]
    list_filter =["name"]
admin.site.register(Posts,PostRegister)
admin.site.register(Contacts,ContactRegister)