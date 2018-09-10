from time import sleep
print('======Cronometro=====')
sleep(3)

v1 = int(input('Tempo: '))
for x in range(0, v1, -1):
	sleep(1)
	print(v1)
print('ola mundo')
