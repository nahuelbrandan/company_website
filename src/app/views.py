from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserForm, LoginForm, AddProductForm
from .models import Room
from termcolor import cprint

company_name = "Company Name"


class HomeView(View):
    def get(self, req):
        context = {
            'is_authenticated': req.user.is_authenticated,
            'username': req.user.username,
            'company_name': company_name
        }
        return render(req, 'home.html', context)


class RegisterView(View):
    def get(self, req):
        context = {
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
            cprint(user, 'magenta')
            if user is not None:
                cprint("Entro a User", 'magenta')
                login(req, user)
                messages.info(req, 'Loggin correcto. Ingresando.')
                return redirect('home')
            else:
                cprint("Not User", 'magenta')

                messages.info(req, 'El usuario o contraseña son incorrectos. Vuelva a intentar')
                return redirect('login')


class LogoutView(View):
    def get(self, req):
        logout(req)
        return HttpResponse('Saludos, esperamos que vuelva pronto.')


class AddRoomView(View):
    def get(self, req):
        context = {
            'form': AddProductForm(),
            'company_name': company_name
        }
        return render(req, 'add_product.html', context)

    def post(self, req):
        form = AddProductForm(req.POST)
        Room.objects.create(**form.cleaned_data)
        return HttpResponse('Listo perro!')


class MeView(View):
    def get(self, req):
        context = {
            'company_name': company_name,
            'username': req.user.username,
            'user': req.user,
            'is_authenticated': req.user.is_authenticated
        }
        return render(req, 'me.html', context)
