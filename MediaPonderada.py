n1 = float(input('Digite sua 1° nota:' ))
n2 = float(input('Digite sua 2° nota:' ))
n3 = float(input('Digite sua 3° nota:' ))
p1 = int(input('Digite o 1° peso: '))
p2 = int(input('Digite o 2° peso: '))
p3 = int(input('Digite o 3° peso: '))

mp = (n1*p1 + n2*p2 + n3*p3)/(p1 + p2 + p3)

print('Está é sua média ponderada: {:.2f}'.format(mp) )