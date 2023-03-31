principal = [[], []]
valor = 0

for c in range(0, 7):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        principal[0].append(valor)
    else:
        principal[1].append(valor)

print('=-'*20)
    
print(f'Os valores pares digitados foram: {sorted(principal[0])}')
print(f'Os valores ímpares digitados foram: {sorted(principal[1])}')
