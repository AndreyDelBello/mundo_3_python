num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))

base = num1, num2, num3, num4

if 9 in base:
    num9 = base.count(9)
    print(f'O valor 9 apareceu {num9} vezes')
else:
    print('O valor 9 não foi digitado')
    
if 3 in base:
    num3 = base.index(3)
    print(f'O valor 3 apareceu {num3+1}º posição')
else:
    print('O valor 3 não foi digitado') 
    
print('Os valores pares digitados foram:',end=' ')

for par in base:
    if par % 2 == 0:
        print(f'{par}', end=' ')
