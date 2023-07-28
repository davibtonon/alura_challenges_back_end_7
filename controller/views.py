from django.shortcuts import render
from controller.models import Depoimentos, Destinos
from controller.serializers import DepoimentosSerializers, DestinosSerializers
from rest_framework import generics, viewsets
# Create your views here.

class DepoimentosViewSet(viewsets.ModelViewSet):
    """Classe para cria as views dos depoimentos"""

    queryset = Depoimentos.objects.all()
    serializer_class = DepoimentosSerializers


class DepoimentosAleatoriosViewSet(generics.ListAPIView):
    """Função para seleciona 3 depoimentos aleatorios"""

    def get_queryset(self):
        queryset = Depoimentos.objects.order_by('?')[0:3]
        return queryset
    
    serializer_class = DepoimentosSerializers


class DestinosViewSet(viewsets.ModelViewSet):
    "Classe para exibir os destinos"
    
    queryset = Destinos.objects.all()
    serializer_class = DestinosSerializers