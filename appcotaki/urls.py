"""pjcotaki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView

from appcotaki.views import (ClienteCreateView, ClienteListView,
                             ComissaoCreateView, ComissaoListView,
                             FabricanteCreateView, FabricanteListView,
                             MaterialCreateView, MaterialListView)

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('cliente_create', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente_list_todos', ClienteListView.as_view(),
         name='cliente_list_todos'),
    path('cotacao_create', views.CotacaoCreate, name='cotacao_create'),
    path('cotacao_cliente_list/<str:nom_cliente>',
         views.CotacaoClienteListView, name='cotacao_cliente_list'),
    path('pedido_cliente_list/<str:nom_cliente>',
         views.PedidoClienteListView, name='pedido_cliente_list'),
    path('comissao_create', ComissaoCreateView.as_view(), name='comissao_create'),
    path('comissao_list_todos', ComissaoListView.as_view(),
         name='comissao_list_todos'),
    path('fabricante_create', FabricanteCreateView.as_view(),
         name='fabricante_create'),
    path('fabricante_list_todos', FabricanteListView.as_view(),
         name='fabricante_list_todos'),
    path('material_create', MaterialCreateView.as_view(),
         name='material_create'),
    path('material_list_todos', MaterialListView.as_view(),
         name='material_list_todos'),
]
