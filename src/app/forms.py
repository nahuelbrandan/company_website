from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(label='Nombre', max_length=100, required=False)
    last_name = forms.CharField(label='Apellido', max_length=100, required=False)
    username = forms.CharField(label='Usuario', max_length=100, required=True)
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(label='Email', required=True)


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100, required=True)
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput(), required=True)


class AddRoomForm(forms.Form):
    title = forms.CharField(label='Titulo', max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    address = forms.CharField(max_length=100, required=True)
    image = forms.ImageField(required=True)
