
from django.urls import path

from app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('add_service/', views.AddServiceView.as_view(), name='add_service'),
    path('me/', views.MeView.as_view(), name='me'),

    path('product/<int:product_id>/', views.ProductView.as_view(), name='product'),
    path('service/<int:service_id>/', views.ServiceView.as_view(), name='service'),
]
