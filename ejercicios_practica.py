#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def ej1():
    # Line Plot
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = list(range(-10, 11, 1))

    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]
    y3 = [i**4 for i in x]
    

    gs = gridspec.GridSpec(3, 1)     
    fig = plt.figure()
    fig.suptitle('ej 1', fontsize=16)

    ax1 = fig.add_subplot(gs[0, :])  
    ax2 = fig.add_subplot(gs[1, :])  
    ax3 = fig.add_subplot(gs[2, :])  
    
    

    ax1.plot(x, y1, color='white', label='y1 = x^2')
    ax1.set_facecolor('black')
    ax1.legend()
    ax1.grid()

    ax2.plot(x, y2, color='darkblue', label='y2 = x^3')
    ax2.set_facecolor('whitesmoke')
    ax2.legend()
    ax2.grid('solid')

    ax3.plot(x, y3, color='black', label='y3 = x^4')
    ax3.set_facecolor('orange')
    ax3.legend()
    ax3.grid(ls = 'dashed')
    
    
    plt.show()
    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección


def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:

    # Realizar dos gráficos que representen
    # y1 = sin(x)
    # y2 = cos(x)
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x

    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.
   
    x = np.arange(0, 4*np.pi, 0.1)

    y1 = np.cos(x)
    y2 = np.sin(x)


    fig = plt.figure()
    fig.suptitle('ej 2', fontsize=16)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.Scatter(x, y1, c='red', label = 'y1 = cos(x)')
    ax1.set_facecolor('whitesmoke')
    ax1.grid('solid')
    ax1.legend()
    ax2.Scatter(x, y2, c='black', label = 'y2 = sen(x)')
    ax2.set_facecolor('whitesmoke')
    ax2.grid('solid')
    ax2.legend()
    plt.show()


def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]

    fig = plt.figure()
    fig.suptitle('ej 3', fontsize=16)
    ax1 = fig.add_subplot(1, 1, 1)
    

    ax1.bar(lenguajes, performance, label='lenguajes')
    ax1.set_facecolor('pink')
    ax1.grid(ls='dashed')

    ax1.legend()


    plt.show()

   

    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.


def ej4():
    
    
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }

    # El gráfico debe tener usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico

    

    fig = plt.figure()
    fig.suptitle('ej 4', fontsize=16)
    ax = fig.add_subplot()

    explode = (0.1, 0, 0, 0, 0, 0, 0)

    ax.pie(uso_lenguajes.values(), labels=uso_lenguajes.keys(), explode=explode, 
           autopct='%1.1f%%', shadow=True, startangle=90
           )
    ax.axis('equal')
    plt.show()

    
def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]

    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valoresde "X" e "Y" para poder utilizar
    # el line plot y observar la señal

    signal_x = [i*step for i in range(sample_size)]
    signal_y = [math.sin(i*step) for i in range(sample_size)]

    fig = plt.figure()
    fig.suptitle('ej 5', fontsize=14)
    ax = fig.add_subplot()

    ax.plot(signal_x, signal_y, c='darkred', marker='^', ms=10, label='sen')
    ax.legend()
    ax.grid()
    
    ax.set_facecolor('whitesmoke')
    plt.show(block=False)


    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7
    filter_signal = [y for y in signal_y if  abs(y) > 0.7]

    filter_signal_x = [i*step for i in filter_signal]
    filter_signal_y = [math.sin(i*step) for i in filter_signal]

    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot
    
    #--------Como seria con Numpy?-------------------------------------------------
    #mask = abs(signal_y[:, 1]) > 0.7
    #filter_signal = signal_y[mask, :]

    #filter_signal_x = filter_signal[:, 0]
    #filter_signal_y = filter_signal[:, 1]
    #---------------------------------------------------------
    
    
    
    fig = plt.figure()
    fig.suptitle('ej 5', fontsize=14)
    ax = fig.add_subplot()

    ax.plot(signal_x, signal_y, color='b', marker='^', label='signal')
    ax.scatter(filter_signal_x, filter_signal_y, color='r', marker='*', label='filter signal')
    ax.grid('solid')

    ax.set_facecolor('whitesmoke')
    ax.set_title("Ej 5")
    

    ax.legend()
    plt.show()

    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?
    #--------------no estoy seguro si quedo bien esto ultimo, 
    # la señal filtrada marca dos puntos nomas--------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
