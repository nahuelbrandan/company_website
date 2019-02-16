
from django.urls import path

from app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add_product/', views.AddRoomView.as_view(), name='add_product'),
    path('me/', views.MeView.as_view(), name='me'),
]
