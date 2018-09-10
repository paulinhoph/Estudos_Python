numero = int(input('Digite um numero:'))
if numero % 2 == 0:
    resposta = 'par'
else:
    resposta = 'impar'
print('Seu número,{0} é {1}'.format(numero, resposta))
