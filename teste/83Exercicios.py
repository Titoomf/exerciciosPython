expresao = str(input('Digite a expressao: '))
pilha = list()
for simbolo in expresao: # para cada simbolo, ele vai pegar cada um simbolo do parentese
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop() # remove o ultimo elemento de uma lista
        else:
            pilha.append(')')
            break # para o laço
if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta errada!')
