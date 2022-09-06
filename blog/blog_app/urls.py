from django.urls import path
from blog_app.views import create_article, list_article, create_ad, search_articles, article_id, Coment_id, About

urlpatterns = [
    path('create-article/', create_article, name="create_article"),
    path('list-article/', list_article, name="list_article"),
    # path('list-author/', list_author, name="ListAuthor" ),
    path('create-ad/', create_ad, name='Advertising'),
    path('search-article/', search_articles, name="search"),
    # path('create-author/', create_author, name='Author')
    path('coment_id/<int:pk>', Coment_id, name= 'comment_id'),
    path('article_id/<int:pk>', article_id, name= 'article_id'),
    path('About/', About, name='ABOUT')
    
]