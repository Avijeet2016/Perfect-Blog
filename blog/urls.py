from django.contrib import admin
from django.urls import path
from .views import post_list, post_detail,  catwise_post, category_list, update_category, delete_category, create_category, blog_post_list, blog_post_detail, update_blog_post, delete_blog_post, create_blog_post

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='home'),
    path('<slug:slug>', post_detail, name='post-detail'),
    path('catwise/post/<str:cat_name>', catwise_post, name='catwise-post'),
    path('category/list', category_list, name='category-list'),
    path('update/category/<int:id>', update_category, name='update-category'),
    path('delete/category/<int:id>', delete_category, name='delete-category'),
    path('create/category', create_category, name='create-category'),

    path('post/list', blog_post_list, name='blog-post-list'),
    path('post/detail/<int:id>', blog_post_detail, name='blog-post-detail'),
    path('update/post/<int:id>', update_blog_post, name='update-blog-post'),
    path('delete/post/<int:id>', delete_blog_post, name='delete-blog-post'),
    path('create/blog/post', create_blog_post, name='create-blog-post'),
]
