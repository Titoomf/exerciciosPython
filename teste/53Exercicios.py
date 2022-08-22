frases = str(input('Digite uma frase: ')).strip().upper()
palavra = frases.split() # vai dividir as palavras Split
junto = ''.join(palavra) #aqui ele tira os espacos e junta as palavras desconsiderando o espaco
inverso = ''
for letra in range(len(junto) - 1, -1, -1): # a ultima letra pegamos com len,
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALINDROMO!')
else:
    print('A frase digitada nao é um palindromo!')
