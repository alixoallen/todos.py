numero=int(input('qual o numero vai digitar ?'))
u=numero//1%10
d=numero//10%10
c=numero//100%10
m=numero//1000%10
print('sua unidade é de {}'.format(u))
print('sua dezena é de {:.0f}'.format(d))
print('sua centena é de {:.0f}'.format(c))
print('seu milhar é de {:.0f}'.format(m))

