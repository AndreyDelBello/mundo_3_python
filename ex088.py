# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta.

import random
import time

print('-='*9)
print('JOGO NA MEGA SENA')
print('-='*9)

jogos = int(input('QUantos jogos você quer que eu sorteie? '))
lista = list()
lista.sort()

print('====== SORTEANDO JOGOS ======')
for i in range(1, jogos+1):
  lista.append(random.sample(range(1, 61), k = 6))
  lista.sort()
  print(f'jogo {i}: {lista}')
  time.sleep(1)
  lista.clear()
print('BOA SORTE!!!')

