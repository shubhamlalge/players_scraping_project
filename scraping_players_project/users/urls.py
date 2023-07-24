from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [

    path('users/post/', views.CreateUser.as_view(), name='user_post'),
    path('users/update/<int:pk>/', views.RetrieveUpdate.as_view(), name='user_update_id'),
    path('users/delete/<int:pk>/', views.RetrieveDelete.as_view(), name='user_delete_id'),
    path('users/list/', views.ListUser.as_view() , name='user_list'),
    path('users/login/', views.Login.as_view(), name='user_login'),
    path('users/logout/', views.Logout.as_view(), name='user_logout'),



]
