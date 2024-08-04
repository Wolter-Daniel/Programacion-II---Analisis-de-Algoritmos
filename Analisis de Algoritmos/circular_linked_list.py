'''
    Linked list.
    Practica Analisis de Algoritmos Computacionales.
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

class Nodo (object):
    def __init__ (self, dato = None, prev = None, prox = None):
        self.dato = dato
        self.prev = prev
        self.prox = prox

class Circular_linked_list (object):
    def __init__(self):
        self.prim = None
        self.last = None
