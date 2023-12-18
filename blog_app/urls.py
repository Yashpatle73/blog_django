from django.urls import path

from . import views

app_name='blog_app'


urlpatterns = [
    path('', views.list_of_articles, name='list_of_articles'),
    
]