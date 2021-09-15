from datetime import date
ano=int(input('qual o ano que deseja saber ?: coloque 0 para saber o ano atual: '))
if ano==0:
    ano=date.today().year
if ano%4==0 and ano %100 != 0 or ano % 400==0:
    print('o ano de {} é bissexto!'.format(ano))
else:
    print('infelizmente o ano não é bissexto')    