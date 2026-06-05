from django.test import TestCase
from django.urls import reverse
from landing.models import Registro

class FlujoRegistroTest(TestCase):

    def test_registro_crea_usuario(self):
        response = self.client.post(reverse("registrar"), {
            "nombre": "Nubia",
            "correo": "nubia@test.com"
        })

        self.assertEqual(response.status_code, 302)  # redirección a verificar
        self.assertTrue(Registro.objects.filter(correo="nubia@test.com").exists())

    def test_verificacion_correcta(self):
        registro = Registro.objects.create(
            nombre="Nubia",
            correo="nubia@test.com",
            codigo="1234",
            verificado=False
        )

        response = self.client.post(reverse("verificar", args=["nubia@test.com"]), {
            "codigo": "1234"
        })

        registro.refresh_from_db()
        self.assertTrue(registro.verificado)
