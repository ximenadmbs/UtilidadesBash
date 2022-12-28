print(10)
print(10.5)

print('Hola Mundo')

#logico (buliano)
#False apagado, True activado
True
False

#listas
['homa mundo', 10, 'hola2', 10.1,]

#Diccionarios
print(type({
    "nombre":"Ryan",
    "apellido":"ray",
    "nick":"fazt"
}))

#variables
name = 'Fazt'
print(name)

name = None
print(name)

x, libro = 100, "50 sombras"
print(x, libro)


#strings
myStr = 'hola Mundo'
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('hola', 'bye'))
print(myStr.replace('hola', 'bye').upper())

#imprimir la fecha
import datetime
horaYfecha = datetime.datetime.now()
print(horaYfecha)
print(horaYfecha.strftime('%d/%m/%Y %H:%M:%S'))

