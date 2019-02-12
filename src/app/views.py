from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserForm, LoginForm, AddRoomForm
from .models import Room


class HomeView(View):
    def get(self, req):
        return render(req, 'home.html')


class RegisterView(View):
    def get(self, req):
        form = UserForm()
        return render(req, 'register.html', {'form': form})

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
        form = LoginForm()
        return render(req, 'login.html', {'form': form})

    def post(self, req):
        form = LoginForm(req.POST)
        user = authenticate(**form.cleaned_data)
        if user is None:
            messages.info(req, 'El usuario o contraseña son incorrectos. Vuelva a intentar')
            return redirect('login')
        else:
            login(req, user)
            messages.info(req, 'Loggin correcto. Ingresando.')
            return redirect('home')


class AddRoomView(View):
    def get(self, req):
        form = AddRoomForm()
        return render(req, 'add_room.html', {'form': form})

    def post(self, req):
        form = AddRoomForm(req.POST)
        Room.objects.create(**form.cleaned_data)
        return HttpResponse('Listo perro!')
