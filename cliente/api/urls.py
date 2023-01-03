from django.urls import path
#from django.conf.urls import url
from django.urls import include, re_path

from rest_framework import routers
from rest_framework.routers import DefaultRouter
from cliente.api.views import (MuncipioListAV, MunicipioDetalleAV, ClienteListAV, DepartamentoDetalleAV,
                               ClienteList, MuncipioWithDepartamentoAV, MunicipioDepartamentoLS, DepartamentoListAV,
                               UsuarioDepartamento, ClienteLS, DepartamentoRetrieve, DepartamentoVS, ClienteDetail)

router = routers.DefaultRouter()
router.register('cliente', ClienteLS, basename='cliente')


urlpatterns=[
    path('', include(router.urls)),
   # path('departamento/', DepartamentoVS.as_view(), name='departamento_list'),    
    #path('departamento/<int:pk>/', DepartamentoLS.as_view(), name='departamento_detail'),
    #path('departamento/', DepartamentoListAV.as_view(), name='departamento_list'),    
    #path('departamento/<int:pk>/', DepartamentoDetalleAV.as_view(), name='departamento_detail'),
    path('municipio/', MuncipioListAV.as_view(), name='municipio_list'),
    path('municipio/<int:pk>', MunicipioDetalleAV.as_view(), name='municipio_detail'),
    #path('cliente/<int:pk>', ClienteLS.as_view(), name='cliente_list'),
    path('clientes/', ClienteListAV.as_view(),  name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetail.as_view(),  name='cliente-detail'),
    #path('departamentos/add/<str:username>/', UsuarioDepartamento.as_view(), name='usuario-departamento'),
    path('departamentos/add/', UsuarioDepartamento.as_view(), name='usuario-departamento'),
    
    
   #    path('articulo/<int:pk>', ArticuloDetalleAV.as_view(), name='articulo_detalle'),
]