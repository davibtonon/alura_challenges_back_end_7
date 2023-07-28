from rest_framework import serializers
from controller.models import Depoimentos, Destinos

class DepoimentosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Depoimentos
        fields = ['depoimento', 'nome_da_pessoa', 'foto']


class DestinosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destinos
        fields = ['foto', 'nome', 'preco']