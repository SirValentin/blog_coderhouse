from django.urls import path
from blog_app.views import create_article, list_article

urlpatterns = [
    path('create-article/', create_article, name="create_article"),
    path('list-article/', list_article, name="list_article"),
]