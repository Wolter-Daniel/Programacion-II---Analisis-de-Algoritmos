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
        '''Insertar elemento al comienzo de la lista'''
        new_nodo = Nodo(dato = data)
        if self.prim == None:
            new_nodo.prev = self.prim
            new_nodo.prox = self.prim
            self.prim = new_nodo
            self.last = new_nodo

        if self.prim != None:
            new_nodo.prev = self.last
            new_nodo.prox = self.prim
            self.prim.prev = new_nodo
            self.last.prox = new_nodo
            self.prim = new_nodo
            

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
