# Company_website
Página web empresarial. Además de informar sobre la empresa, esta la posibilidad de mostrar y vender sus productos y/o servicios. Si bien está desarrollada para una empresa en particular, haciendo cambios en el contenido se podría adaptar para cualquier otra.Desarrollada en Python con Django.

### Autor:
Nahuel Brandan. (nahuelbrandan123@gmail.com)

## Instalación:

1.  Verificar que Python esta instalado (version 3 es requerida): `python -V`
2.  Dentro de la raiz del directorio, crear un entorno virtual con el siguiente comando: `virtualenv -p python3 env`
3.  Ingresar a éste entorno virtual ejecutando: `source env/bin/activate`
4.  Chequeamos las librerias instaladas en éste nuevo entorno ejecutando: `pip3 list`
    Deberían ser sólo las básicas, obteniendo:
    
        Package    Version
        ---------- -------
        pip        19.0.1
        setuptools 40.8.0
        wheel      0.32.3

5.  Instalar django: `pip3 install django pillow django-livereload-server django-crispy-forms termcolor`
6.  [Éste paso sólo lo realizo yo por única vez para crear el proyecto.]
    `django-admin startproject compartir_alquiler`
8.  Ejecutar `$ bash first_time.sh`. Se te pedirá que ingreses usuario y contraseña para crear tu cuenta como admin.
9.  Ejecutar `$ python manage.py runserver` para correr el programa en localhost. Ingresa desde tu navegador a `http://127.0.0.1:8000`
    para que automáticamente se refresque la página al haber algún cambio ejecutar primero `% python manage.py livereload` en una terminal, y en otra `$ python manage.py runserver`

    #python manage.py createsuperuser;

Sólo los Super usuarios pueden agregar productos de venta.
