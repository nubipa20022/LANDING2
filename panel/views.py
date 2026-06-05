from django.shortcuts import render
from landing.models import Registro

def dashboard(request):
    total = Registro.objects.count()
    verificados = Registro.objects.filter(verificado=True).count()
    pendientes = Registro.objects.filter(verificado=False).count()

    return render(request, 'panel/dashboard.html', {
        'total': total,
        'verificados': verificados,
        'pendientes': pendientes,
    })

def registros(request):
    registros = Registro.objects.all().order_by('-creado')
    return render(request, 'panel/registros.html', {'registros': registros})
