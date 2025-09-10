from django.urls import path
from . import views

appname = "viacep"

urlpatterns = [
    path('', views.base, name='base'),
    path('consulta_cep/', views.consulta_cep, name='consulta_cep')

]