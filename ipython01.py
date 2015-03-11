# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

''' 
    Ejercicio: 01 Botella de Ron
    Autores: Emilio Bello Villanueva y Juan Carlos de la Torre Macías
    Fecha: 10/03/2015
    Asignatura: Sistemas Distribuidos
    Comentarios:
        Para la resolución del ejercicio, se ha optado por la creación de una lista
        que se inicia en el número 99 y acaba en el 0 y es recorrida mediante un bucle
        for (recordemos que la condición se cumplirá mientras la variable numero no tome 
        el valor cero). Con el parámetro -1 indicamos que recorra la lista con saltos de 
        un solo elemento en sentido descendente.
        La variable numero es de tipo int, por lo que debemos hacerle un casting a string
        para poder usarla con print, se ha optado por el uso del operador %, si bien se podría
        haber optado por:
        print str(numero) + "bottles of ..."
'''
for numero in range(99,0,-1):
    print "\t%s bottles of beer on the wall, %s bottles of beer.\n\tTake one down, pass it around, %s bottles of beer on the wall.\n" %(numero,numero,numero-1)

# <codecell>


