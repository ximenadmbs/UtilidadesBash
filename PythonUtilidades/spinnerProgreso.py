# Instalar modulo:
# pip install progress

# Declara un objeto de la clase Spinner(). En cada ciclo una hélice
# gira hasta que se completa la lectura del archivo creado en el
# ejemplo anterior. Cuando se completa la lectura se muestra el 
# número total de caracteres encontrados de cada tipo ('X'/'O').
# Una hélice muestra que un proceso se está ejecutando pero no 
# no ayuda a prever su final.
# El módulo tienes otras clase para declarar objetos similares:
# PieSpinner, MoonSpinner, LineSpinner y PixelSpinner.

from progress.spinner import Spinner
import os, time, random

datos = os.getcwd()+os.sep+"datos.txt"

spinner = Spinner('Leyendo: ')
cuenta_X = 0
cuenta_O = 0
archivo = open(datos, "r")
while True: 
    linea = archivo.readline()
    if linea:
        for caracter in linea:
            if caracter == 'X':
                cuenta_X+=1
            elif caracter == 'O':
                cuenta_O+=1
    else:
        break
    time.sleep(0.1)
    spinner.next()
    
print(' X=', cuenta_X, 'O=', cuenta_O)
archivo.close