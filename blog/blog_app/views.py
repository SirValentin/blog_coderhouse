
from turtle import title
from django.shortcuts import render, redirect
from blog_app.forms import FormArticle, FormAd
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog_app.models import Article, Advertising
from django.contrib.auth.models import User
from users.models import User_profile

@login_required
def create_article(request):
    
    if request.method == 'POST':
        form = FormArticle(request.POST, request.FILES)

        if form.is_valid():
            Article.objects.create(
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                image = form.cleaned_data['image'],
                author = User.objects.get(id=request.user.id)
            )

            return redirect (list_article)
    elif request.method == 'GET':
        form = FormArticle()
        context = {'form':form}
        return render(request, 'new_article.html', context=context)

@login_required
def create_ad(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = FormAd(request.POST, request.FILES)
            print(request.FILES)
            if form.is_valid():
                Advertising.objects.create(
                    company = form.cleaned_data['company'],
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    image = form.cleaned_data['image']
                )

                return redirect (list_article)
        elif request.method == 'GET':
            form = FormAd()
            context = {'form':form}
            return render(request, 'new_ad.html', context=context)
    return redirect('/blog/list-article/')

# @login_required
# def create_author(request):
    
#     if request.method == 'POST':
#         form = FormAuthor(request.POST)

#         if form.is_valid():
#             Author.objects.create(
#                 name = form.cleaned_data['name'],
#                 email = form.cleaned_data['email'],
#                 description = form.cleaned_data['description']
#             )

#             return redirect (list_author)
#     elif request.method == 'GET':
#         form = FormAuthor()
#         context = {'form':form}
#         return render(request, 'new_author.html', context=context)        

@login_required
def list_article(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
        'ad': Advertising.objects.all()
    }
    return render(request, 'list_article.html', context=context)

# @login_required
# def list_author(request):
#     authors = Author.objects.all()
#     context = {
#         'authors':authors
#     }
#     return render(request, 'list_author.html', context=context)

@login_required
def search_articles (request):
      search = request.GET['search']
      articles = Article.objects.filter(title__icontains=search)
      context = {'articles': articles}
      print(articles)
      return render(request, 'search_article.html', context=context )


