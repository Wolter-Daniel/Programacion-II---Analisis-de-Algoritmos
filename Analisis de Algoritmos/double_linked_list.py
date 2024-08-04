class Nodo (object):
    def __init__ (self, dato = None, prev = None, prox = None ):
        self.dato = dato
        self.prev= prev
        self.prox = prox

class Double_linked_list (object):
    '''Craer un objeto'''
    def __init__ (self):
        self.prim = None
        self.last = None

    def add_at_front (self, data):
        '''Insertar elemento al comienzo de la lista'''
        new_nodo = Nodo(dato = data, prev = None, prox = self.prim)
        if self.prim != None:
            self.prim.prev = new_nodo
        else:
            self.prim = new_nodo
        if self.last == None:
            self.last = self.prim
          

    def print_list (self):
            '''Metodo para mostrar lista.'''
            nodo = self.prim
            while nodo != None :
                print("Dato:", nodo.dato)
                nodo = nodo.prox

    def print_revert_list (self):
            '''Metodo para mostrar la lista invertida.'''
            nodo = self.last
            while nodo != None :
                print("Dato:", nodo.dato)
                nodo = nodo.prev
