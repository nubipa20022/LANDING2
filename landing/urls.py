from django.urls import path
from . import views
from .views import ping

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('registrar/', views.registrar, name='registrar'),
    path('verificar/<str:correo>/', views.verificar, name='verificar'),
    path('reenviar/<str:correo>/', views.reenviar, name='reenviar'),
    path('login/', views.login_admin, name='login'),
    path('panel/', views.panel, name='panel'),
    path("api/validar/", views.validar_datos, name="validar_datos"),
    path("api/generar-codigo/", views.generar_codigo_test, name="generar_codigo_test"),
    path("api/registrar-test/", views.registrar_test, name="registrar_test"),
    path("api/verificar-test/", views.verificar_test, name="verificar_test"),
    path("ping/", ping, name="ping"),
]



