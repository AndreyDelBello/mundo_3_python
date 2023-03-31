from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10))

print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
    
print(f'\nO maior valor da sorteado é: {max(numeros)}')
print(f'O menor valor da sorteado é: {min(numeros)}')













# ================================================================= #
# USANDO LISTAS SERIA:

'''
lista = []
for c in range(1, 6):
    c = randint(1, 9)
    lista.append(c)
    
print(f'Os valores sorteados foram: {lista}')
print(f'O maior valor da sorteado é: {max(lista)}')
print(f'O menor valor da sorteado é: {min(lista)}')
'''
