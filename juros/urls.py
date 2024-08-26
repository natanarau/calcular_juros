from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular_juros, name='calcular_juros'),
]