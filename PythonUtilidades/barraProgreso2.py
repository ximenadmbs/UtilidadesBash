# Instalar modulo:
# pip install progress

# Declara un objeto de la clase ChargingBar(). Cuando comienza
# el bucle aparece una barra punteada y durante los ciclos los 
# puntos "∙" son sustituidos por el carácter "█" hasta alcazar
# el 100%.

from progress.bar import Bar, ChargingBar
import os, time, random

bar2 = ChargingBar('Instalando:', max=100)
for num in range(100):
    time.sleep(random.uniform(0, 0.2))
    bar2.next()
bar2.finish()