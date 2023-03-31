galera = list()
dado = list()
mai = men = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('peso: ')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de', end=' ')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {men}Kg. Peso de', end=' ')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')



