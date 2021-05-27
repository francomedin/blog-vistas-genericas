from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('detail/<pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('update/<pk>', views.PostUpdateView.as_view(), name='post_update'),


]
