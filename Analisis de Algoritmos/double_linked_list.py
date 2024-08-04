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
        self.prim = new_nodo
        if self.last == None:
            self.last = self.prim
          
    def add_at_end (self, data):
        new_nodo = Nodo (dato = data, prev = self.last, prox = None)
        if self.prim == None:
              self.add_at_front(data)
              return
        else:
            self.last.prox = new_nodo
        self.last = new_nodo

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

