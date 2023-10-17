from django.contrib import admin
from .models import blog_posts

@admin.register(blog_posts)
class blog_admin(admin.ModelAdmin):
    list_display=['id','title','desc']