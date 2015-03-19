# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>



''' 
    Ejercicio: 02 Pokemon
    Autores: Emilio Bello Villanueva y Juan Carlos de la Torre Macías
    Fecha: 17/03/2015
    Asignatura: Sistemas Distribuidos
'''


# Cargamos en memoria el contenido del fichero
archi=open('pokemon.txt','r')
datos=archi.readlines()
archi.close()


original = [] # Lista que contendrá las palabras originales
temporal = [] # Lista que contendrá la cadena que se está analizando en cada momento
solucion = [] # Lista que contendrá la cadena más larga existente

for linea in datos:                     #Recorremos cada línea leída
    for palabra in linea.split(' '):    #Recorremos cada elemento de la línea separado por espacios
        if palabra[-1] == "\n":         #Si el elemento termina con el carácter fin de línea
            palabra = palabra[:-1]          #Eliminamos el carácter fin de línea encontrado
        original.append(palabra)        #Incluimos la palabra en la lista original

i = 0
while i < len(original):        #Iniciará la búsqueda con todas las palabras de la lista original
    palabra = original[i]           #Almacenamos la primera palabra de la secuencia a buscar
    temporal.append(palabra)        #Incluimos en la secuencia la primera palabra
    j = 0
    while j < len(original):    #Recorrerá toda la lista desde el inicio cada vez que añadamos una nueva palabra
        if (original[j][0] == palabra[-1]) and (original[j] not in temporal): #Si cumple la premisa y no ha sido incluida todavía
            temporal.append(original[j])    #Incluimos la palabra
            palabra = original[j]           #Pasa a ser nuestra nueva palabra cuyo último caracter debemos buscar
            j=-1                            #Para buscar la siguiente palabra otra vez desde el inicio
        j=j+1                   #Seguimos recorriendo la lista en busca de la siguiente palabra
    if len(temporal)>len(solucion):     #Si la solución parcial encontrada es mayor que la solución almacenada la sustituimos
        solucion = temporal[:]
    temporal = []                       #Vaciamos la lista temporal
    i=i+1                               #Pasamos a la siguiente palabra de la lista original para iniciar la secuencia de nuevo
    
print "La lista mas larga encontada es: \n%s"%(solucion)

# <codecell>
