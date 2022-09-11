sal = float(input('Digite o seu salário: '))
peraumento = float(input('Digite o seu percentual de aumento: '))

novosal =  sal * peraumento + sal
aumento = sal * peraumento

print('Seu aumento foi de: {:.2f}'.format(aumento))
print('Esté é o seu novo salário: {:.2f}'.format(novosal))