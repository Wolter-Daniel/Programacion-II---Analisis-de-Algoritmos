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
            new_nodo.prev = new_nodo
            new_nodo.prox = new_nodo
            self.prim = new_nodo
            self.last = new_nodo

        if self.prim != None:
            new_nodo.prev = self.last
            new_nodo.prox = self.prim
            self.prim.prev = new_nodo
            self.last.prox = new_nodo
            self.prim = new_nodo

    def add_at_end (self, data):
        '''Insertar elemento al final de la lista'''
        new_nodo = Nodo(dato = data)

        if self.prim == None:
            new_nodo.prev = new_nodo
            new_nodo.prox = new_nodo
            self.prim = new_nodo
            self.last = new_nodo

        if self.prim != None:
            new_nodo.prev = self.last
            new_nodo.prox = self.prim
            self.last.prox = new_nodo
            self.prim.prev = new_nodo
            self.last = new_nodo
            

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

    def search (self, data):
        if self.prim != None:
            nodo = self.prim
            while nodo != self.last:
                if nodo.dato == data:
                    print("Encontrado!!")
                    return nodo.dato
                else:
                    nodo = nodo.prox
            else:
                print("El dato no existe!!!")
                return

    def delete (self, data):
        '''Metodo para eliminar un dato'''
        nodo = self.prim

        while nodo:
            if nodo.dato == data:
                if nodo == self.prim:
                    self.prim = nodo.prox
                    if self.prim != None:
                        self.prim.prev = self.last
                    else:
                        self.last = None

                elif nodo == self.last:
                    self.last = nodo.prev
                    if self.last != None:
                        self.last.prox = self.prim
                    else:
                        self.prim = None

                else:
                    nodo.prev.prox = nodo.prox
                    nodo.prox.prev = nodo.prev
                    print("Dato Borrado")
                    return
            else:
                nodo = nodo.prox 
        else:
            print("Dato no existente")
