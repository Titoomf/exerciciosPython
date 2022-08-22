'''import math
angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {:.2f} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = math.sin(math.radians(angulo))
print('O angulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.sin(math.radians(angulo))
print('A tangente de {:.2f} tem a TANGENTE de {:.2f}'.format(angulo, tangente))'''

from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
print('O angulo de {:.2f} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {:.2f} tem a TANGENTE de {:.2f}'.format(angulo,tangente))