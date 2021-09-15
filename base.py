a=int(input('digite um numero inteiro:'))
print('escolha as opções:')
print('[ 1 ]Binario')
print('[ 2 ] OCTAL')
print('[ 3 ] hexadecimal')
escolha=int(input('sua escolha é ? :'))
aa=bin(a)
bb= oct(a)
cc=hex(a)
if escolha== 1: 
    print('{} convertido para binario fica {}'.format(a,aa))
if escolha== 2:
    print('{} convertido para octal fica {}'.format(a,bb))
elif escolha== 3:
    print('{} convertido para hexadecimal fica {}'.format(a,cc))

    #poderia nao usar a lista e apenas rodar o programa lendo variaveis dentro das condições 
    ### if escolha==1
        #print('{} bla bla bla {}'.format(a,bin(a))) dessa forma funciona tb        