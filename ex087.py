matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma_terceira_coluna = 0
maior = 0

#Estruturando a matriz e fazendo o usuario inserir os valores
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
            
# Soma os valores da terceira coluna
for l in range(0, 3):
    soma_terceira_coluna += matriz[l][2]
  
# Maior valor da segunda linha
for c in range(0, 3):  
    if matriz[1][c] == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]

# Formatando a visualização da matriz
print("-="*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print("-="*30)

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da tarceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior}.')

