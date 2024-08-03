class Nodo (object):
    def __init__ (self, dato = None, prev = None, prox = None ):
        self.dato = dato
        self.prev= prev
        self.prox = prox

class Double_linked_list (object):
    '''Craer un objeto'''
    def __init__ (self):
        self.prim = None

    def add_at_front (self, data):
        new_nodo = Nodo(dato = data, prev = None, prox = self.prim)
        if self.prim != None:
            self.prim.prev = new_nodo
        self.prim = new_nodo
          

    def print_list (self):
            '''Metodo para mostrar lista.'''
            nodo = self.prim
            while nodo != None :
                print("Prev:",nodo.prev, "Nodo:", nodo.dato, "prox:", nodo.prox)
                nodo = nodo.prox

