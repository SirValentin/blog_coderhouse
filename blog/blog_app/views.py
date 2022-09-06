
from turtle import title
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect, get_object_or_404
from blog_app.forms import FormArticle, FormAd
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog_app.models import Article, Advertising
from django.contrib.auth.models import User
from users.models import User_profile
from django.contrib.contenttypes.models import ContentType
from .forms import FormComentarios
from .models import Coment
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages


def About(request):
     return render(request, 'about.html', context={} )


def Coment_id(request, pk):

    instance = get_object_or_404(Coment, pk=pk)

    context = {
        "comentario": instance
    }
    return render (request, 'Coments/instance.html', context)

def article_id(request, pk):
    instance = get_object_or_404(Article, pk=pk)

    inicializar_datos = {
        "content_type" : instance.get_content_type,
        "object_id": instance.id
    }

    form = FormComentarios(request.POST or None, initial = inicializar_datos)
    
    if form.is_valid():
        models = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=models)
        obj_id = form.cleaned_data.get("object_id")
        text_data = form.cleandes_data.get("text")

        comentarios = Coment.objects.get_or_create(

            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            text = text_data
        )
        
        return HttpResponseRedirect(comentarios.content_object.get_absolute_url())

     
        
    context = {
        'form':form,
        'instance':instance
    }
         
    return render(request, 'Coments/coments.html', context)

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
        'articles':articles
    }
    print(context)
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




