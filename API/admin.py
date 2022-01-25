from django.contrib import admin
from .models import InstagramUser, Ipost

@admin.register(Ipost)
class Postadmin(admin.ModelAdmin):
    list_display = ['id','caption', 'location', 'can_comment', 'tags', 'image',]

@admin.register(InstagramUser)
class UserAdmin(admin.ModelAdmin):
    list_display=['id', 'username', 'E_mail', 'bio',  'likedpost']