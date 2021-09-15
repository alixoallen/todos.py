dias=int(input('quantos dias ficou com o carro?'))
km=float(input('quantos km voce percorreu com ele?'))
d= (dias*60) + (km* 0.15)
print('o valor a pagar sera de R${} '.format(d))