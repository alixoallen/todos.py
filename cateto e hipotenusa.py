from  math import sqrt
hypo=float(input('qual o seu primeiro cateto oposto? '))
hypos=float(input('qual o seu segundo cateto adjacente?'))
cnt= sqrt(hypo**2+hypos**2)


print('segundo o teorema de pitagoras, e segundo a formula seu cateto {} e seu cateto{}, sao iguas a {}'.format(hypo,hypos,cnt))

#usando somento o hypot da biblioteca math e lendo as duas variaveis que declarei seria mais facil executar