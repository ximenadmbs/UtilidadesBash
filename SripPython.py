import time

print('\n')

print('Ingresa tu nombre: ')
nombre = input()

cadena = '-' * 50
caracter = '#'

b = 0
for i in range(100):
    if(i % 2 == 0):
        x = list(cadena)
        x[b] = caracter
        cadena = "".join(x)

    print(f'[{cadena}]{i+1}%', end='\r')
    time.sleep(0.02)