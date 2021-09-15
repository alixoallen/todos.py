from random import randint
computer=randint(0,5)
print('pensei no numero{}'.format(computer))#gera um numero aleatorio, ou faz o computador """"""pensar"""""""""""""""
escolha=int(input('digite um numero:'))
if escolha == computer:
    print('parabens voce acertou!')
else: 
    print('ora ora voce é meio pessimo nisso!')    