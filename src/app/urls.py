
from django.urls import path

from app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('add_room/', views.AddRoomView.as_view(), name='add_room'),
]
