from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.PostList.as_view()),
    # path('<int:pk>/', views.single_post_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('create_post/', views.PostCreat.as_view())
    # path('update_post/<int:pk>/', views.PostUpdate.as_view())
]
