from django.shortcuts import render
from controller.models import Depoimentos, Destinos
from controller.serializers import DepoimentosSerializers, DestinosSerializers
from rest_framework import generics, viewsets, filters
from rest_framework.response import Response

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
    filter_backends  = [filters.SearchFilter]
    search_fields = ['nome']

    def list(self, request, *args, **kwargs):
        # Função que modifica o list para apresentar uma messagem de erro caso não encontre nda

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        if not queryset.exists():
            return Response({"message": "Nenhum resultado encontrado."})
        
        return Response(serializer.data)