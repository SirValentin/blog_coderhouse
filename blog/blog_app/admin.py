from django.contrib import admin
from blog_app.models import Article, Advertising

@admin.register(Article)
class Articles_admin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author']

@admin.register(Advertising)
class Advertising(admin.ModelAdmin):
    list_display = ['company', 'title', 'description', 'is_active', 'image']
