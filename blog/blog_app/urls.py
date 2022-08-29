from django.urls import path
from blog_app.views import create_article, list_article, create_ad, search_articles

urlpatterns = [
    path('create-article/', create_article, name="create_article"),
    path('list-article/', list_article, name="list_article"),
    # path('list-author/', list_author, name="ListAuthor" ),
    path('create-ad/', create_ad, name='Advertising'),
    path('search-article/', search_articles, name="search"),
    # path('create-author/', create_author, name='Author')
]