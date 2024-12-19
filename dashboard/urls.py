from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/',views.categories, name ='categories'),
    path('categories/add',views.categories_add, name ='categories_add'),
    path('categories/edit/<int:pk>',views.categories_edit, name ='categories_edit'),
    path('categories/remove/<int:pk>',views.categories_remove, name ='categories_remove'),

    path('posts/', views.posts, name="posts"),
    path('posts/add', views.posts_add, name="posts_add"),
    path('posts/edit/<int:pk>',views.posts_edit, name ='posts_edit'),
    path('posts/remove/<int:pk>',views.posts_remove, name ='posts_remove'),

    path('users',views.users, name ='users'),
    path('users/add',views.users_add, name ='users_add'),
    path('users/edit/<int:pk>',views.users_edit, name ='users_edit'),
    path('users/remove/<int:pk>',views.users_remove, name ='users_remove'),



]