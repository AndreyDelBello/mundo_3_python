lista = []
n1 = n2 = n3 = n4 = n5 = 0
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionando a posição {pos} da lista...')
                break
            pos += 1
            
print('=-'*30)
print(f'Os valores digitados em ordem foram {lista}')
        
            