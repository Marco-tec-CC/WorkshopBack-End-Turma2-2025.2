from django.urls import path
from .views import ViaCepDeleteView, ViaCepDetailView, ViaCepListView, ViaCepFormView
from . import views


#app_name = "viacep"

urlpatterns = [
    path('', views.base, name='base'),
    path('listar/', ViaCepListView.as_view(), name='list'),
    path('consultar/', ViaCepFormView.as_view(), name='form'),
    path('detalhe/<int:pk>/', ViaCepDetailView.as_view(), name='detail'),
    path('deletar/<int:pk>/', ViaCepDeleteView.as_view(), name='delete'),

]