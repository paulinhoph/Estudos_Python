velocidade = int(input('Qual a velocidade do carro:'))
if velocidade > 80:
    multa = 7.0 * (velocidade - 80)
    print('Você recebeu uma multa de R${0:.1f} por dirigir a {1}Km/h em uma pista de 80Km/h'.format(multa,velocidade))