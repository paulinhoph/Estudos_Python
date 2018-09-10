# ***PYTHON PAULO HENRIQUE****

print('=== DESAFIO 16 ===')

n = int(input('Digite um número até 9999:'))
print('== MÉTODO INT ==')
print('Unidade = {}'.format(n % 10))
print('Dezena = {}'.format((n // 10) % 10))
print('Centena = {}'.format((n // 100) % 10))
print('Milhar = {}'.format(n // 1000))
print('== MÉTODO STRING ==')
n = '000' + str(n)  # para que possamos escrever 1, 23 ou 395
print('Unidade = {}'.format(n[-1])) # Também daria pra usar n[len(n)-1]
print('Dezena = {}'.format(n[-2]))
print('Centena = {}'.format(n[-3]))
print('Milhar = {}'.format(n[-4]))