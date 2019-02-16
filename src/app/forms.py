from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(label='Nombre', max_length=100, required=False)
    last_name = forms.CharField(label='Apellido', max_length=100, required=False)
    username = forms.CharField(label='Usuario', max_length=200, required=True)
    password = forms.CharField(label='Contraseña', max_length=200, widget=forms.PasswordInput(), required=True)
    email = forms.EmailField(label='Email', required=True)


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=200, required=True)
    password = forms.CharField(label='Contraseña', max_length=200, widget=forms.PasswordInput(), required=True)


class AddProductForm(forms.Form):
    title = forms.CharField(label='Titulo', max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    price = forms.IntegerField(label="Precio", required=True)
    principal_image = forms.ImageField(label="Imagen principal",required=True)
    aditional_image = forms.ImageField(label="Imagen adicional",required=False)
    aditional_image_2 = forms.ImageField(label="Imagen adicional 2",required=False)
    aditional_image_3 = forms.ImageField(label="Imagen adicional 3",required=False)
