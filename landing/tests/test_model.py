from django.test import TestCase
from landing.models import Registro

class RegistroModelTest(TestCase):

    def test_creacion_registro(self):
        registro = Registro.objects.create(
            nombre="Nubia",
            correo="nubia@test.com",
            verificado=False
        )

        self.assertEqual(registro.nombre, "Nubia")
        self.assertFalse(registro.verificado)
