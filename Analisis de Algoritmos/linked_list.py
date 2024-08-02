'''Linked list nodo.
    Practica Analisis de Algoritmos Computacionales.
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''
class _Nodo (object):

    #Constructor

    def __init__ (self, dato = None, prox = None ):
        self.dato = dato
        self.prox = prox

    def verLista (nodo):
        while nodo:
            print(nodo.dato)
            nodo = nodo.prox

class _linked_list (Object):
    def __init__ (self):
        self.prim = None

    # Método para agregar elementos en el frente de la linked list

    def add_at_front(self, dato):
        self.prim = _Nodo(data = dato, prox = self.prim)

    # Método para verificar si la estructura de datos esta vacia

    def is_empety (self):
        return False if self.prim == None else True
    
    

v3 = _Nodo ("Manzanas")
v2 = _Nodo ("Peras", v3)
v1 = _Nodo ("Bananas", v2)

#Referencia del principio de la lista.

lista = v1 

#print(v1.dato)
#print(v2.dato)
#print(v3.dato)

_Nodo.verLista(lista)