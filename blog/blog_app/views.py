from django.shortcuts import render

from blog_app.models import Article

def create_article(request):
    new_article = Article.objects.create(
        title = 'Primer articulo',
        content = 'Primer articulo de la app que emocion',
        author = 'vale'
    )
    context = {
        'new_article': new_article
    }
    return render(request, 'new_article.html', context=context)

def list_article(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'list_article.html', context=context)
