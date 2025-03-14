#!/usr/bin/env python
'''
Numpy [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"

import numpy as np
import random 


def ej1():
    print ('Ejercicio 1:\n')
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro

    # potencia_2 = lambda x:......
    # pot_3 = potencia_2(3)
    potencia_2 = lambda x:2**x
    pot_3 = potencia_2 (3)
    print (pot_3)
    print("")


    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "potencia_2" dentro del map, debe colocar
    # directamente la lambda.

    # Lista de numeros
    numeros = [1, -5, 4, 3]
    numeros_potencia = list(map(lambda x: 2**x, numeros))
    print(numeros_potencia)
    print ("")

    # numeros_potencia = list(map....)


def ej2():
    print("Ejercicio 2: \n")
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que retorne el tamaño
    # (len) de un string pasado como parámetro

    # len_string = lambda......

    len_string = lambda x: len (x)
    frase = len ("El mail del contribuyente es: fperezchada@gmail.com")
    print (frase)
    print("")


    # 2)
    print("Ejercicio 2.2: \n")
    # Lista de string
    palabras = ['Inove', 'casa', 'programacion']
    
    
    
    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto em cata iteración
    # de la lista de textos
    # El resultado (el len de cada palabra) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line"
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "len_string" dentro del map, debe colocar
    # directamente la lambda.

    # palabras_len = list(map....)
    palabras_maps= list(map(len, palabras))
    print(palabras_maps)

def ej3():
    print('Práctica de comprensión de listas')
    # 1)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá tener un tamaño de 11
    # números, conteniendo del 0 al 10 inclusive

    lista_0_10 = range(-1,10)
    
    lista_comp = [x + 1 for x in lista_0_10]
    print(lista_comp)

    # 2)
    print("")
    print("Ejercicio 3.2")
    # Generar una lista a partir de comprensión de listas,
    lista5_0_10 = range(0,11)
    
    lista5_comp = [5*x for x in lista5_0_10]
    print(lista5_comp)

    # 3)
    print("")
    print("Ejercicio 3.3")
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener 10 números aleatorios,
    # estos números deberán estar entre el rango 1 al 30 representando
    # números posibles de un mes (los números pueden repetirse).
    # NOTA: Importar le módulo random y utiliza randrange
    # o randint para generar números aleatorios.z
    # https://docs.python.org/3/library/random.html

    dias_mes = range(0,30)
    listarandom= [x + 1 for x in dias_mes]
    print(random.sample(listarandom,10))

def ej4():
    print("")
    print("Ejercicio 4.1")
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.
    
    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']
    lista_num_int = []
    for x in list_numeros_str:
        if x.isdigit() == True:
            valor = int(x)
        else:
            valor = 0
        lista_num_int.append(valor)

    print(lista_num_int)

    print("\nLo hice sin comprimir porque me costo bastante sacarle la vuelta de rosca \n")

    print ("\nMetodo comprimido\n")

    lista_num_int_2= [int(x) if x.isdigit() == True else 0 for x in list_numeros_str]
    print (lista_num_int_2, "\n")

    print("pregunta 2\n")
    
    list_negativos_numeros_str = ['5', '2', '3', '', '7', 'NaN']
    
    
    lista_negativo_2 = [int(x) * (-1) if x.isdigit() == True else 0 for x in list_negativos_numeros_str]
    print(lista_negativo_2)



    # ¿Ya terminaron el ejercicio? Si, me llevo mas de 1 dia!!! 
    # ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? Sorprendente no?    


def ej5():
    # Utilizar comprensión de listas para filtrar

    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]

     

    # La lista accesso contiene los números de ID de personal
    # que ingresaron por ese molinete

    # 1)
    # Generar una lista por comprensión de la lista "accesos"
    # una lista que solo contenga (filtrado) los ID de personal
    # entre 1 al 10 inclusive, se desea separar del grupo de accesos
    # los ID entre el 1 y 10.
    # De la lista resultante informar cuantas personas/personal
    # comprendido en dicho rango pasó por ese molinete

    personal_1_10 = []

    for x in accesos:
        if x >=1 and x <11:
            personal_1_10.append(x)
        else:
            pass
            
    print("Las personas que pasaron el molinete son:", personal_1_10, "de un tal de", len(personal_1_10), "personas \n")
    
    personal_1_10_comp = [x for x in accesos if x>=1 and x <11]
    print("las personas que pasaron fueron los ID:",personal_1_10_comp, "la cantidad de personas son:", len(personal_1_10_comp))


    # 2)
    # Generar una lista por comprensión de la listas "accesos"
    # cuyo ID de personal esté dentro de los ID válidos para ingresar
    # por ese molinete:
    id_validos = [3, 4, 7, 8, 15]
    # Debe generar una nueva lista basada en "accesos" filtrada por los ID
    # aprobados en "id_validos".
    # TIP: Utilizar el operador "in" para chequear si un ID de accesos está
    # dentro de "id_validos"

    personal_valido = [x for x in accesos if x in id_validos]
    print("Los Id validos son:", personal_valido, "\n")


def ej6():
    print('Ejercicio de funciones Numpy')
    # Arme un array con el método np.arange
    # el cual este acotado entre 0 y 1000
    # De dicho array calcular las siguientes operaciones:

    eje= np.arange(1,1001)
    

    # 1)
    # Calcular la suma de todos los elementos en el array
    # utilizar el método "sum" de numpy

    suma = np.sum(eje)
    print (suma)

    # 2)
    # Calcular la diferencia de todos los elementos en el array
    # utilizar el método "diff" de numpy

    diferencia = np.diff(eje)
    print(diferencia)

    # 3)
    # Utilizar la funcion "where" para reemplazar los números múltiplos
    # de "5" por un "0"
    # Ojo: ¿Que operador matematico utilizará para saber si un número es
    # múltiplo de "5"? Ese operador ya lo conoce y lo viene utilizando
    # bastante para saber si un número es múltiplo de "2"

    nuevo_array = np.asanyarray(eje)
    eje3= np.where((eje % 5) == 0, nuevo_array, 0)
    print(eje3)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
    ej6()
