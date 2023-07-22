from django.shortcuts import render
from controller.models import Depoimentos
from controller.serializers import DepoimentosSerializers
from rest_framework import generics, viewsets
# Create your views here.

class DepoimentosViewSet(viewsets.ModelViewSet):
    queryset = Depoimentos.objects.all()
    serializer_class = DepoimentosSerializers


class DepoimentosAleatoriosViewSet(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = Depoimentos.objects.order_by('?')[0:3]
        return queryset
    
    serializer_class = DepoimentosSerializers