from django.contrib import admin
from .models import Category, NewsArticle, Comment

admin.site.register(Category)
admin.site.register(NewsArticle)
admin.site.register(Comment)
