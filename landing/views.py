from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Registro
from .utils import validar_nombre, validar_correo
from .email_utils import enviar_codigo, enviar_notificaciones
import random

def formulario(request):
    return render(request, "index.html", {"errores": {}, "nombre": "", "correo": ""})

def registrar(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")

        errores = {}

        if not validar_nombre(nombre):
            errores["nombre"] = "Solo letras y espacios permitidos."

        if not validar_correo(correo):
            errores["correo"] = "Formato de correo inválido."

        if Registro.objects.filter(correo=correo).exists():
            errores["correo"] = "Este correo ya está registrado."

        if errores:
            return render(request, "index.html", {
                "errores": errores,
                "nombre": nombre,
                "correo": correo
            })

        codigo = str(random.randint(100000, 999999))

        Registro.objects.create(
            nombre=nombre,
            correo=correo,
            codigo=codigo,
            verificado=False
        )

        enviar_codigo(correo, codigo)

        return redirect(reverse("verificar", args=[correo]))

def verificar(request, correo):
    registro = Registro.objects.filter(correo=correo).order_by("-id").first()

    if not registro:
        return render(request, "verificar.html", {
            "correo": correo,
            "error": "No se encontró registro para este correo."
        })

    if request.method == "POST":
        codigo_ingresado = request.POST.get("codigo").strip()

        if registro.verificado:
            return render(request, "verificar.html", {
                "correo": correo,
                "ok": "Este correo ya está verificado."
            })

        if registro.codigo == codigo_ingresado:
            registro.verificado = True
            registro.save()
            return render(request, "success.html")

        return render(request, "verificar.html", {
            "correo": correo,
            "error": "Código incorrecto. Intenta nuevamente."
        })

    return render(request, "verificar.html", {"correo": correo})

def reenviar(request, correo):
    registro = Registro.objects.filter(correo=correo).first()

    if registro:
        nuevo_codigo = str(random.randint(100000, 999999))
        registro.codigo = nuevo_codigo
        registro.verificado = False
        registro.save()
        enviar_codigo(correo, nuevo_codigo)

        return render(request, "verificar.html", {
            "correo": correo,
            "ok": "Hemos reenviado el código a tu correo."
        })

    return render(request, "verificar.html", {
        "correo": correo,
        "error": "No se pudo reenviar el código."
    })

def login_admin(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        password = request.POST.get("password")

        user = authenticate(request, username=usuario, password=password)

        if user:
            login(request, user)
            return redirect("panel")

        return render(request, "login.html", {"error": "Credenciales inválidas"})

    return render(request, "login.html")

@login_required
def panel(request):
    correos = Registro.objects.filter(verificado=True).values_list("correo", flat=True)

    if request.method == "POST":
        asunto = request.POST.get("asunto")
        mensaje = request.POST.get("mensaje")

        enviar_notificaciones(correos, asunto, mensaje)

        return render(request, "panel.html", {
            "correos": correos,
            "ok": "Notificaciones enviadas"
        })

    return render(request, "panel.html", {"correos": correos})

# Create your views here.
from django.http import JsonResponse
from .utils import validar_nombre, validar_correo

def validar_datos(request):
    nombre = request.GET.get("nombre", "")
    correo = request.GET.get("correo", "")

    return JsonResponse({
        "nombre_valido": validar_nombre(nombre),
        "correo_valido": validar_correo(correo)
    })

def generar_codigo_test(request):
    import random
    codigo = str(random.randint(100000, 999999))
    return JsonResponse({"codigo": codigo})

def registrar_test(request):
    from .models import Registro
    nombre = request.GET.get("nombre", "Test")
    correo = request.GET.get("correo", "test@example.com")

    registro = Registro.objects.create(
        nombre=nombre,
        correo=correo,
        codigo="123456",
        verificado=False
    )

    return JsonResponse({
        "id": registro.id,
        "correo": registro.correo,
        "codigo": registro.codigo
    })

def verificar_test(request):
    correo = request.GET.get("correo")
    codigo = request.GET.get("codigo")

    registro = Registro.objects.filter(correo=correo).first()

    if not registro:
        return JsonResponse({"error": "No existe"}, status=404)

    if registro.codigo == codigo:
        registro.verificado = True
        registro.save()
        return JsonResponse({"ok": True})

    return JsonResponse({"ok": False})

from django.http import HttpResponse

def ping(request):
    return HttpResponse("pong")

