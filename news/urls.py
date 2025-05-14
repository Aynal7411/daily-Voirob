from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_articles, name='category_articles'),
    path('news/<slug:slug>/', views.article_detail, name='article_detail'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
