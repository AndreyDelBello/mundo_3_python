lista = []
listaP = []
listaI = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listaP.append(n)
    else:
        listaI.append(n)
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break

print('=-'*30)
print(f'A lista completa é {lista}')
print(f'A lista de Pares é {listaP}')
print(f'A lista de Ímpares é {listaI}')    