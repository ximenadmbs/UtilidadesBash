# Instalar modulo:
# pip install progress

# Declara un objeto de la clase Countdown(). En cada ciclo un 
# contador que comienza en 100 va disminuyendo su valor hasta
# alcanzar 0, que marca el fin del bucle.
# El módulo tiene otras clases para declarar objetos 
# similares: Counter, Pie y Stack

from progress.counter import Countdown
import time

contador = Countdown("Contador: ")
for num in range(100):
    contador.next()
    time.sleep(0.05)

print()