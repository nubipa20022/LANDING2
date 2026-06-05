from django.db import models

class Registro(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    codigo = models.CharField(max_length=6)
    verificado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.correo

