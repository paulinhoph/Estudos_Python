from random import randrange
print('Estou pensando em um numero de 0 até 6')
numero = randrange(0, 6)
chute = int(input('Digite seu chute:'))
if chute == numero:
    print('Isso ai, Você acertou')
else:
    print('Não foi dessa vez o numero era {}'.format(numero))