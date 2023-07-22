from rest_framework import serializers
from controller.models import Depoimentos

class DepoimentosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Depoimentos
        fields = ['depoimento', 'nome_da_pessoa', 'foto']