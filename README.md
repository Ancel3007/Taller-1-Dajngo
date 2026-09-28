# Sistema de productos

Aplicación web desarrollada con Django para registrar y listar productos almacenados en una base de datos SQLite.

## Tecnologías
- Python
- Django
- SQLite
- HTML
- Git y GitHub

## Funcionalidades
- Listado de productos.
- Registro de nuevos productos.
- Validación de precio y cantidad.
- Almacenamiento mediante Django ORM.
- Navegación entre listado y formulario.

## Ejecución en Windows CMD

```cmd
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/

Formulario: http://127.0.0.1:8000/productos/nuevo/

## Git

```cmd
git init
git add .
git commit -m "feat: implementar registro y listado de productos"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```
