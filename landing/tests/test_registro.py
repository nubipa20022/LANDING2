from django.test import TestCase
from landing.utils import validar_nombre, validar_correo

class ValidacionesTest(TestCase):

    def test_validar_nombre_correcto(self):
        self.assertTrue(validar_nombre("Nubia"))

    def test_validar_nombre_incorrecto(self):
        self.assertFalse(validar_nombre("Nubia123"))

    def test_validar_correo_correcto(self):
        self.assertTrue(validar_correo("test@gmail.com"))

    def test_validar_correo_incorrecto(self):
        self.assertFalse(validar_correo("correo-malo"))
