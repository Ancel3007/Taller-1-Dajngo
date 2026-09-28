from django.test import TestCase
from .models import Producto


class ProductoModelTest(TestCase):
    def test_crear_producto(self):
        producto = Producto.objects.create(
            nombre='Producto de prueba',
            categoria='General',
            precio=10000,
            cantidad=5,
        )
        self.assertEqual(str(producto), 'Producto de prueba')
