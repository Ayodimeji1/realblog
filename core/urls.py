from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('archives/', views.archives, name='archives'),
    path('about', views.about, name='about')
]