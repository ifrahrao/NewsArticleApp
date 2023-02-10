from django.urls import path
from news_app import views

urlpatterns = [
    path('', views.news_app, name='news_app'),
    path('news_category/',views.news_category,name='news_category'),
    path('author/',views.author,name='author')
]