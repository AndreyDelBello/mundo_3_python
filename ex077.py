palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

# Percorrendo cada palavra na tupla
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')