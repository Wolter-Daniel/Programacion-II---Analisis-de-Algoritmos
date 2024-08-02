'''Linked list nodo.
    Practica Analisis de Algoritmos Computacionales.
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''
class Nodo (object):
    def __init__(self, dato = None, prox = None ):

        #Constructor

        self.dato = dato
        self.prox = prox

v3 = Nodo (234)
v2 = Nodo (875, v3)
v1 = Nodo (999, v2)

print(v1.dato)
print(v2.dato)
print(v3.dato)
