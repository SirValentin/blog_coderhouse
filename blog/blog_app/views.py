
from turtle import title
from django.shortcuts import render, redirect
from blog_app.forms import FormArticle, FormAd, FormComent
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog_app.models import Article, Advertising, Coment
from django.contrib.auth.models import User
from users.models import User_profile

@login_required
def About(request):
     return render(request, 'about.html', context={} )
    
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

@login_required
def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/blog/list-article/')

@login_required
def see_article(request, pk):
    if request.method == 'GET':
        article = Article.objects.get(pk=pk)
        coments = Coment.objects.filter(article=article)
        context = {'article':article, 'coments':coments}
        return render(request, 'article.html', context=context)
    if request.method == 'POST':
        form = FormComent(request.POST)
        
        if form.is_valid():
            Coment.objects.create(
                text = form.cleaned_data['text'],
                article = Article.objects.get(pk=pk),
                user = User.objects.get(id=request.user.id)
            )

            return redirect (f'/blog/see-article/{pk}')
        

@login_required
def list_article(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
        'ad': Advertising.objects.all()
    }
    return render(request, 'list_article.html', context=context)

@login_required
def search_articles (request):
      search = request.GET['search']
      articles = Article.objects.filter(title__icontains=search)
      context = {'articles': articles}
      print(articles)
      return render(request, 'search_article.html', context=context )


