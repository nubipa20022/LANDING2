from django.core.mail import send_mail

def enviar_codigo(correo, codigo):
    asunto = "Código de verificación"
    mensaje = f"Tu código de verificación es: {codigo}"
    remitente = "nubipa20022@gmail.com"
    send_mail(asunto, mensaje, remitente, [correo])

def enviar_notificaciones(correos, asunto, mensaje):
    remitente = "nubipa20022@gmail.com"
    for correo in correos:
        send_mail(asunto, mensaje, remitente, [correo])
