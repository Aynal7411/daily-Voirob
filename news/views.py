from django.shortcuts import render, get_object_or_404
from .models import NewsArticle, Category

def home(request):
    featured = NewsArticle.objects.filter(featured=True)
    latest = NewsArticle.objects.order_by('-created_at')[:5]
    return render(request, 'home.html', {'featured': featured, 'latest': latest})

def article_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug)
    return render(request, 'article_detail.html', {'article': article})

def category_articles(request, category_id):
    articles = NewsArticle.objects.filter(category_id=category_id)
    return render(request, 'category_articles.html', {'articles': articles})
