## Sistema de productos

Aplicación web desarrollada con Django para registrar y listar productos almacenados en una base de datos SQLite.

## Tecnologías
- Python
- Django
- SQLite
- HTML
- Git y GitHub

## Funcionalidades
- Listado de productos y categoria.
- Registro de nuevos productos y categoria.
- Crud de productos y categoria.
- Validación de precio y cantidad.
- Almacenamiento mediante Django ORM.
- Navegación entre listado y los distintos formularios.

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

Listado/Productos: http://127.0.0.1:8000/productos/lista/

Listado/Categoria: http://127.0.0.1:8000/categoria/lista/

## Git

```cmd
git init
git add .
git commit -m "Se actualiza el proyecto"
git branch -M main
git remote add origin https://github.com/Ancel3007/Taller-1-Dajngo.git
git push -u origin main
```