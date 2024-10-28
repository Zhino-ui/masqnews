from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index , name="homepage"),
    path('blog_item/<int:pk>/', views.blog_item, name="blog_item"),
    path('category/<slug:slug>/', views.category_page, name="category_page"),
    path('search/', views.search, name="search"),
    path('adverts/', views.adverts, name='adverts'),
]
