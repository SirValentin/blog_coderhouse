from django.contrib import admin
from blog_app.models import Article, Advertising, Coment

@admin.register(Article)
class Articles_admin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author']

@admin.register(Advertising)
class Advertising(admin.ModelAdmin):
    list_display = ['company', 'title', 'description', 'is_active', 'image']

@admin.register(Coment)
class Advertising(admin.ModelAdmin):
    list_display = ['user', 'article', 'text']
