from math import ceil, floor
inteiro= float(input('digite o numero :'))
r=  ceil (inteiro)
f= floor(inteiro)
print('o seu numero arredondado para cima fica {}, e arredondado para baixo fica {}'.format(r,f))
#poderia usar na biblioteca math o ///trunc///, obteria resposta mais rapido, ou apenas usar a função interna do python que tira a fração do numero e a mostra inteira /////int dentro do format///

