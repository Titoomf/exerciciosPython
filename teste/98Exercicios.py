from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=' * 50)
    print(f'Contagem de {i} ate {f} pulando de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ',
                  flush=True)  # aqui eu vou desligar o buffer de tela para que ele faca corretamente
            sleep(0.5)
            cont += p
        print('Fimm')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIMMMM!!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)  # aqui ele nao vai fazer pq o inicio é maior que o fim, teremos que faze um if para verificar
print('=' * 50)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
