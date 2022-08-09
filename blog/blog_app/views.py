
from turtle import title
from django.shortcuts import render, redirect
from blog_app.forms import FormArticle, FormAd, FormAuthor
from django.http import HttpResponse

from blog_app.models import Article, Advertising,Author

def create_article(request):
    
    if request.method == 'POST':
        form = FormArticle(request.POST)

        if form.is_valid():
            Article.objects.create(
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                author = form.cleaned_data['author']
            )

            return redirect (list_article)
    elif request.method == 'GET':
        form = FormArticle()
        context = {'form':form}
        return render(request, 'new_article.html', context=context)


def create_ad(request):
    
    if request.method == 'POST':
        form = FormAd(request.POST)

        if form.is_valid():
            Advertising.objects.create(
                company = form.cleaned_data['company'],
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description']
            )

            return redirect (list_article)
    elif request.method == 'GET':
        form = FormAd()
        context = {'form':form}
        return render(request, 'new_ad.html', context=context)


def create_author(request):
    
    if request.method == 'POST':
        form = FormAuthor(request.POST)

        if form.is_valid():
            Author.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                description = form.cleaned_data['description']
            )

            return redirect (list_author)
    elif request.method == 'GET':
        form = FormAuthor()
        context = {'form':form}
        return render(request, 'new_author.html', context=context)        

def list_article(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'list_article.html', context=context)

def list_author(request):
    authors = Author.objects.all()
    context = {
        'authors':authors
    }
    return render(request, 'list_author.html', context=context)


def search_articles (request):
      search = request.GET['search']
      articles = Article.objects.filter(title__icontains=search)
      context = {'articles': articles}
      print(articles)
      return render(request, 'search_article.html', context=context )


