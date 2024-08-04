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

    def add_at_front (self, data):
        new_nodo = Nodo(dato= data, prev = self.last, prox = self.prim)
        self.prim = new_nodo

        if self.last == None:
            self.last = self.prim

    def print_list (self):
        if self.prim != None:
            nodo = self.prim
            while nodo != self.last:
                print("Dato: ", nodo.dato)
                nodo = nodo.prox
            else:
                print("Dato:",nodo.dato)

    def print_revert_list (self):
         if self.prim != None:
            nodo = self.last
            while nodo != self.prim:
                print("Dato: ", nodo.dato)
                nodo = nodo.prev
            else:
                print("Dato:",nodo.dato)

linked_list = Circular_linked_list()
linked_list.add_at_front("Hola")
linked_list.add_at_front("Mundo")
linked_list.add_at_front("!")
linked_list.add_at_front("!")
linked_list.add_at_front("!")
linked_list.add_at_front("#")
linked_list.print_list()