from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='panel_dashboard'),
    path('registros/', views.registros, name='panel_registros'),
]
