'''Linked list nodo.
    Practica Analisis de Algoritmos Computacionales.
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''
class _Nodo (object):

    #Constructor

    def __init__(self, dato = None, prox = None ):
        self.dato = dato
        self.prox = prox

    def verLista (nodo):
        while nodo:
            print(nodo.dato)
            nodo = nodo.prox

v3 = _Nodo ("Manzanas")
v2 = _Nodo ("Peras", v3)
v1 = _Nodo ("Bananas", v2)

#Referencia del principio de la lista.

lista = v1 

#print(v1.dato)
#print(v2.dato)
#print(v3.dato)

_Nodo.verLista(lista)