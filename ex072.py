cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))
while True:
    if num <= 20 and num >= 0:
        num = cont[num]
        print(f'Você digitou o número {num}')
        break
    else:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))

# ======================================================================================== #

# from num2words import num2words

# num = int(input('Digite um número entre 0 e 20: '))
# while True:
#     if num <= 20 and num >= 0:
#         num_ptbr = num2words(num, lang='pt-br')
#         print(f'Você digitou o número {num_ptbr}')
#         break
#     else:
#         num = int(input('Tente novamente. Digite um número entre 0 e 20: '))

