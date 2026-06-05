import re

def validar_nombre(texto):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", texto))

def validar_correo(correo):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", correo))
