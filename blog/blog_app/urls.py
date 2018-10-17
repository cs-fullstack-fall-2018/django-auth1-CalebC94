from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.userIndex, name='user_index'),
]