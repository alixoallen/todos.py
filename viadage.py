dist=float(input('qual a distancia em km voc irá percorrer na viagem? '))
god=dist*0.50
gud=dist*0.45
if(god<=200): 
    print('sua viagem custara: R$ {:.2f}'.format(god))
else:
    print('sua viagem custara : R$ {:.2f}'.format(gud))