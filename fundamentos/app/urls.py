from django.urls import path
from .views import horario_atual, form_cliente

urlpatterns = [
    path('horario_atual', horario_atual, name='horario_atual'),
    path('form_cliente', form_cliente, name='form_cliente'),
]
