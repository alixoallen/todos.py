casa=float(input('qual o valor dea casa que deseja comprar?'))
salario=float(input('e qual o valor do seu salario?'))
anos=int(input('em quantos anos pretende pagar ?'))
aaa=anos*12
prestação=casa/aaa
if prestação>(30/100*salario):
    print('pra pagar uma casa de R${:.2f}, em {} anos a prestação sera de {:.2f}, assim o valor de emprestimo foi negado!'.format(casa,anos,prestação))
else:
    print('o emprestimo foi concedido com sucesso!')
    #esqueci como fazia a atribuição burro