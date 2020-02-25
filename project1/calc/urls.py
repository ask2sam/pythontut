from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('htmlpage', views.htmlpage, name="htmlpage"),
    path('add', views.add, name="add") 
]
