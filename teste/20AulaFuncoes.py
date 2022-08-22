# aprendendo funcao personalizada
'''def lin():
    print('-=' * 30)


print('CURSO EM VIDEO')
lin()
print('APRENDA PHYTHOM DO ZERO')
lin()
print('CURSO EM VIDEO')
lin()'''

# funcao com parametros

'''def titulo(msg):
    print('-=' * 30)
    print(msg)
    print('=-'* 30)

#programa Principal
titulo(' Curso em Videos ')
titulo('Phytom é muito bom') # esse texto vai para o paramentro da funcao '''


'''def soma(a, b):
    s = a + b
    print(s)


'''''''# programa principal
soma(4, 6)
soma(6, 7)
soma(2, 6)'''''

'''def contador(*num): despacotar seria o usuario digitar varios numero e ele fazer a conta por isso usamos o *
   tamanho = len(num)
   print(f'Recebi os valores {num} e sao ao todo {tamanho} ')


contador(5, 6, 8, 9)
contador(2, 1, 0)
contador(2,5)'''

def dobra(list):
   pos = 0
   while pos < len(list):
      list[pos] *= 2
      pos += 1


valores = [2, 3, 5, 6, 8]
dobra(valores)
print(valores)




