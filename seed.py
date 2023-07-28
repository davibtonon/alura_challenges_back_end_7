# Script para cria os dados fakes para testa a aplicação

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "setup.settings")
django.setup()

from django.db import models
from faker import Faker
import random, decimal
from controller.models import Depoimentos, Destinos


def cria_dados_faker(quantidade=10):
    # Função que cria os depoimentos fakes

    fake = Faker('pt_BR')
    
    for _ in range(quantidade):
        depoimento = fake.paragraph(nb_sentences=2)
        nome_da_pessoa = fake.name()
        numero_foto = str(random.randint(1,10 ))
        foto = 'foto' + numero_foto + '.jpg'

        Depoimentos.objects.create(
            depoimento=depoimento,
            nome_da_pessoa=nome_da_pessoa,
            foto=foto
        )

    print(f"Finalizado foram criados {quantidade} depoimentos")


def cria_destinos_faker(quantidade=20):
    fake = Faker('pt_BR')
    
    for _ in range(quantidade):
        preco = decimal.Decimal(
            fake.pydecimal(left_digits=4, right_digits=2, positive=True))
        nome = Faker().city() # Tenho que melhora isso kk
        numero_foto = str(random.randint(1,10 ))
        foto = 'foto' + numero_foto + '.jpg'

        Destinos.objects.create(
            preco=preco,
            nome=nome,
            foto=foto
        )

    print(f"Finalizado foram criados {quantidade} Destinos")

if __name__ == '__main__':
    print('Escolhar uma opção: ')
    opcao = input('1 = depoimentos\n 2 = Destinos\n')
    opcao = int(opcao)
    if opcao == 1:
        cria_dados_faker(50)
    if opcao == 2:
        cria_destinos_faker()
    else:
      pass