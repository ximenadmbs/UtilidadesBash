# Instalar modulo:
# pip install progress

# Declara un objeto de la clase Bar(). En cada ciclo la barra
# muestra una porción hasta llegar a su máxima longitud en el 
# ciclo 20. La barra se representa con el carácter #

from progress.bar import Bar, ChargingBar
import os, time, random

bar1 = Bar('Procesando:', max=100)
for num in range(100):
    time.sleep(0.2)
    bar1.next()
bar1.finish()