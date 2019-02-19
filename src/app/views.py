from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from os import listdir

from .forms import UserForm, LoginForm, AddProductForm, AddServiceForm
from .models import Product, Service
from termcolor import cprint

import os
from django.conf import settings

company_name = "Nanzi & Cande"


class HomeView(View):
    def get(self, req):
        galery_images = ['images/galery/'+f for f in listdir(os.path.join(settings.BASE_DIR, 'app/static/images/galery/'))]

        context = {
            'title': 'N&C Centro de belleza',
            'is_superuser': req.user.is_superuser,
            'is_authenticated': req.user.is_authenticated,
            'username': req.user.username,
            'company_name': company_name,
            'products': Product.objects.all(),
            'services': Service.objects.all(),
            'galery_images': galery_images
        }
        return render(req, 'home.html', context)


class RegisterView(View):
    def get(self, req):
        context = {
            'title': 'Registro',
            'form': UserForm(),
            'company_name': company_name
        }
        return render(req, 'register.html', context)

    def post(self, req):
        # create a form instance and populate it with data from the req:
        form = UserForm(req.POST)

        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return HttpResponse('/usuario creado exitosamente/')
        else:
            return HttpResponse('/hubo un problema de registro/')


class LoginView(View):
    def get(self, req):
        context = {
            'title': 'Ingresar',
            'form': LoginForm(),
            'company_name': company_name
        }
        return render(req, 'login.html', context)

    def post(self, req):
        form = LoginForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                messages.info(req, 'Loggin correcto. Ingresando.')
                return redirect('home')
            else:
                messages.info(req, 'El usuario o contraseña son incorrectos. Vuelva a intentar')
                return redirect('login')


class LogoutView(View):
    def get(self, req):
        logout(req)
        return redirect('home')


class AddProductView(View):
    def get(self, req):
        context = {
            'title': 'Añadir producto',
            'form': AddProductForm(),
            'company_name': company_name
        }
        return render(req, 'add_product.html', context)

    def post(self, req):
        form = AddProductForm(req.POST, req.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return HttpResponse('Producto agregado con éxito!')
        else:
            return HttpResponse('Lo siento. Hubo algun problema. Vuelva a intentarlo.')


class AddServiceView(View):
    def get(self, req):
        context = {
            'title': 'Añadir servicio',
            'form': AddServiceForm(),
            'company_name': company_name
        }
        return render(req, 'add_service.html', context)

    def post(self, req):
        form = AddServiceForm(req.POST, req.FILES)
        if form.is_valid():
            Service.objects.create(**form.cleaned_data)
            return HttpResponse('Servicio agregado con éxito!')
        else:
            return HttpResponse('Lo siento. Hubo algun problema. Vuelva a intentarlo.')


class ProductView(View):
    def get(self, req, product_id):
        context = {
            'title': 'Producto',
            'product': Product.objects.get(id=product_id),
            'company_name': company_name
        }
        return render(req, 'product.html', context)


class ServiceView(View):
    def get(self, req, service_id):
        context = {
            'title': 'Servicio',
            'service': Service.objects.get(id=service_id),
            'company_name': company_name
        }
        return render(req, 'product.html', context)


class MeView(View):
    def get(self, req):
        context = {
            'title': 'Usuario',
            'company_name': company_name,
            'username': req.user.username,
            'user': req.user,
            'is_authenticated': req.user.is_authenticated
        }
        return render(req, 'me.html', context)
