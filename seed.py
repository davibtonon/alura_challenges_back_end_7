# Script para cria os dados fakes para testa a aplicação

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "setup.settings")
django.setup()

from django.db import models
from faker import Faker
import random
from controller.models import Depoimentos


def cria_dados_faker(quantidade=10):
    # Função que cria os depoimentos fakes

    fake = Faker('pt_BR')
    
    for _ in range(quantidade):
        depoimento = fake.paragraph(nb_sentences=2)
        nome_da_pessoa = fake.name()
        numero_foto = str(random.randint(1,10 ))
        foto = 'foto' + numero_foto + '.jpg'

        # print('Nome', nome_da_pessoa)
        # print('Depoimento: ', depoimento)
        # print('Foto: ', foto)

        Depoimentos.objects.create(
            depoimento=depoimento,
            nome_da_pessoa=nome_da_pessoa,
            foto=foto
        )

    print(f"Finalizado foram criados {quantidade} depoimentos")

if __name__ == '__main__':
    cria_dados_faker(50)