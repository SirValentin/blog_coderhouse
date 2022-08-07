from django.contrib import admin
from blog_app.models import Article

@admin.register(Article)
class Articles_admin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author']
