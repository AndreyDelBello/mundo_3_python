cont = 0
lista = []
r = 'S'
while r in 'S':
    n = int(input('Digite um valor: '))
    cont += 1
    lista.append(n) 
    r = str(input(f'Quer continuar? [S/N] ')).strip().upper()[0]

print('=-'*25)
print(f'Voce digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!') 
else: 
    print('O valor 5 não foi encontrado na lista!')    