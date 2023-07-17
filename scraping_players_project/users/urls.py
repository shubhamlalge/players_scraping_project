from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [

    path('users/post/',views.CreateUser.as_view(),name = 'user_post'),
    path('users/update/<int:pk>',views.RetrieveUpdateDestroyAPIView.as_view(),name = 'user_update_id'),
    path('users/delete/<int:pk>',views.RetrieveUpdateDestroyAPIView.as_view(),name = 'user_delete_id'),
    path('users/list',views.ListUser.as_view(),name = 'user_list'),
    path('users/list/<int:pk>',views.ListUser.as_view(),name = 'user_list_id'),



]
