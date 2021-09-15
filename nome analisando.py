nome=str(input('digite uma frase:')).upper().strip()
print('a letra A, aparece {} vezes'.format(nome.count('A')))
print('a primeira letra aparece na posição {}'.format(nome.find('A')+1))
print('a ultima letra aparece na posição {}'.format(nome.rfind('A')+1))
#execicos de string sao comploexos p minha cabeça