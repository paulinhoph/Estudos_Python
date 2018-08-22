 				# ***PYTHON PAULO HENRIQUE****

 				# ***formatando nome****
print('====== DESAFIO 01 ======')								
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

				# *** valores formatandos ****
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

				# ***Desafio que fiz solo***

print('====== DESAFIO 04 ======')
n = int(input('Número inteiro: '))
a = n-1
s = n+1
print('Analisando o seu valor {}, \n  é o antecessor e o {} \n é o seu sucessor!'.format(a, s))


				# ***DEsafio que fiz solo***

print('====== DESAFIO 05 ======')
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** 2
print('O dobro do seu valor é {}, \n o triplo é {} \n e a raiz quadrada é {}!'.format(d, t, r))			

					# ***DEsafio que fiz solo***

print('====== DESAFIO 06 ======')
nt = float(input('Nota do Teste: '))
np = float(input('Nota da Prova: '))
r = nt + np
print('A sua média é {:.1f}!'.format(r))

					# ***DEsafio que fiz solo***

print('====== DESAFIO 07 ======')
m = int(input('Digite um valor Métrico: '))
cm = m * 100
mm = m * 1000
print('O seu valor convertido em Centímetro são{}cm \nE convertido em Milímetros são{}mm \n!'.format(cm, mm))

					# ***DEsafio que fiz solo***

print('====== DESAFIO07 ======')
m = float(input('Digite um numero em metros para ver quanto o mesmo vale em centímetros e milímetros: '))
cm = m*100
mm = cm*10
print('Esse número: vale {}cm\n{}mm.'.format(cm, mm))

					# ***DEsafio que fiz solo***

print('====== DESAFIO08 ======')
n = float(input('Digite um número para ver sua respectiva tabuada: '))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print('1|  {}'.format(n1))
print('2|  {}'.format(n2))
print('3|  {}'.format(n3))
print('4|  {}'.format(n4))
print('5|  {}'.format(n5))
print('6|  {}'.format(n6))
print('7|  {}'.format(n7))
print('8|  {}'.format(n8))
print('9|  {}'.format(n9))
print('10| {}'.format(n10))

						# ***DEsafio que fiz solo***

print('====== DESAFIO09 ======')
n = float(input('Digite quantos reais você tem para ver quantos dolares você pode comprar: '))
d = n/3.27
print('Você pode comprar U${:.2f} em dolar.'.format(d))

						# ***DEsafio que fiz solo***

print('====== DESAFIO10 ======')
l = float(input('Digite o comprimento em metros da parede: '))
h = float(input('Digite a altura em metros da parede: '))
a = l*h
qt = a/2
print('A área da sua parede é de {}m²,\n sendo que você precisará de \n{}Latas de tinta para pinta-la por completo.'.format (a, qt))


						# ***DEsafio que fiz solo***

print('====== DESAFIO11 ======')
x = float(input('Digite o preço do produto: '))
dx = (x*5)/100
s = x - dx
print('O preço desse produto com um desconto de 5% é\nR${:.2f}'.format(s))

						# ***DEsafio que fiz solo***

print('====== DESAFIO12 ======')
x = float(input('Digite o valor de seu salario: '))
y = (x*50)/100
z = y + x
print('O seu salario com 15%  de aumento iria ser: R${:.2f}'.format(z))