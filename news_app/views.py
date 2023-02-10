from django.shortcuts import render,HttpResponse
from news_app.models import NewsArticle,NewsCategory,Author

def news_app(request):
    news_articles = NewsArticle.objects.all()
    context = {
        'articles': news_articles
    }
    return render(request, 'news_articles.html', context)

def news_category(request):
    news_catogories = NewsCategory.objects.all()
    context = {
        'categories': news_catogories
    }
    return render(request, 'news_category.html', context)

def author(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'authors.html', context)