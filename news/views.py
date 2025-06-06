from django.shortcuts import render,redirect,get_object_or_404
from .models import NewsArticle, Category
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

def home(request):
    featured = NewsArticle.objects.filter(featured=True)
    latest = NewsArticle.objects.order_by('-created_at')[:5]
    return render(request, 'home.html', {'featured': featured, 'latest': latest})

def article_detail(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug)
    return render(request, 'article_detail.html', {'article': article})

def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles =NewsArticle.objects.filter(category=category, published=True)
    return render(request, 'category_articles.html', {'articles': articles, 'category': category})



def search(request):
    query = request.GET.get('q')
    articles = NewsArticle.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'search.html', {'articles': articles, 'query': query})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        # Create new user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Redirect to login page
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or dashboard after successful login
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')  

def user_logout(request):
    logout(request)
    return redirect('home')