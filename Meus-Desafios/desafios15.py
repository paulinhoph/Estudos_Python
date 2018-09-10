print('====== DESAFIO 15 ======')

nome = input('Insira seu nome: ').strip()
letras = len(nome) - nome.count(' ')  # serve para facilitar nas funções extras
dividido = nome.split()  # também serve para facilitar nas funções extras
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Número de letras: {}'.format(letras))
print('Primeiro nome: {}. Ele tem {} letras'.format(dividido[0], nome.find(' ')))
print('Sobrenome: {}. Ele tem {} letras'.format(' '.join(dividido[1:]), letras - nome.find(' ')))