		# ***PYTHON PAULO HENRIQUE****


 	# ***formatando nome****


print('====== DESAFIO 14======')

from math import hypot

co = float(input('Qual o cateto oposto? '))
ca = float (input('Qual o cateto adjacente? '))

hip = hypot(co, ca)

print ('A hipotenusa do triângulo que possui o cateto oposto {} e o cateto adjacente {} é {}'.format(co, ca, hip))


from math import sqrt

co = float(input('Qual o cateto oposto? '))
ca = float (input('Qual o cateto adjacente? '))

hip = (co**2) + (ca**2)

res = sqrt(hip)

print ('A hipotenusa do triângulo que possui o cateto oposto {} e o cateto adjacente {} é {}'.format(co, ca, res))
