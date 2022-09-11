salbase = float(input('Digite o seu salário base: '))

salareceber = (salbase * 5)/100 - (salbase * 7)/100 + salbase

print('O salário que ira receber é: {:.2f}'.format(salareceber))