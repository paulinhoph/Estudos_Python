# ***PYTHON PAULO HENRIQUE****

 				# ***formatando nome****

print('====== DESAFIO 02 ======')
n1 = int(input('um valor: '))
n2 = int(input('outro valor : '))
print('o valor e {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end='')
print('Divisão inteira {} e potência {}'.format(di, e))