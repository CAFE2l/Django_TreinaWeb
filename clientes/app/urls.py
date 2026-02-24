from django.urls import path, include 
from .views import (ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDetailView)

urlpatterns=[
  path("form_cliente", ClienteCreateView.as_view()), 
  path("lista_clientes", ClienteListView.as_view(), name="lista_clientes"),
  path("form_cliente/<int:pk>", ClienteUpdateView.as_view(), name="editar_cliente"),
  path("lista_cliente/<int:pk>", ClienteDetailView.as_view(), name="lista_cliente"),
]
