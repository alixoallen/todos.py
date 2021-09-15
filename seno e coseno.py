import math
angulo= float(input('digite o angulo a ser calculado:'))
seno=math.sin(math.radians(angulo))
print('o seno de {}, é {:.2f}'.format(angulo,seno))
cosseno=math.cos(math.radians(angulo))
print('o cosseno de {} é {:.2f}'.format(angulo, cosseno))
tangente=math.tan(math.radians(angulo))
print('a tangente de {}, é {:.2f}'.format(angulo,tangente ))
#nao soube interpretar a biblioteca, pois o angulo era em graus, entao teria q ser radiano e depois seno cosseno e tangente 