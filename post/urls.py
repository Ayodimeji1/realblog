from django.urls import path

from post import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('comment/reply/', views.reply_page, name='reply')
]