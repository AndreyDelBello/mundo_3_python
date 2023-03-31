lista = []

while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'nN':
            lista_ordenada = sorted(lista)
            print(f'Você digitou os valores {lista_ordenada}')
            break
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'nN':
            lista_ordenada = sorted(lista)
            print(f'Você digitou os valores {lista_ordenada}')
            break