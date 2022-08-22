palavras = ('aprender', 'estudar', 'jogar','assistir','analisar','programar',
            'destacar','python', 'cursos', 'futuro', 'carreira','estruturas'
            'mercado', 'oportunidade', 'praticar', 'gratis', 'linguagem')
for p in palavras: # para cada palavra se faz um lanco de repeticao.
    print(f'\nNa palavra {p.upper()} temos:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')