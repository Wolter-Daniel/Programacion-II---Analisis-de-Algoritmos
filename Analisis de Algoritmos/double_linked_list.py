'''
    Linked list.
    Practica Analisis de Algoritmos Computacionales.
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''
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

    def search (self, data):
        if self.prim != None:
            nodo = self.prim
            while nodo:
                if nodo.dato == data:
                    return nodo.dato
                else:
                    nodo = nodo.prox
            else:
                print("El dato no existe!!!")
                return

    def delete (self, data):
        if self.prim != None:
            nodo = self.prim
            nodo_prev = None 
            while nodo:
                if nodo.dato == data and nodo_prev == None:
                    self.prim = nodo.prox
                    return
                elif nodo.dato == data:
                    nodo_prev.prox = nodo.prox
                nodo_prev = nodo
                nodo = nodo.prox
            else:
               print('El dato a borrar no existe')
               return
        else:
            print("No hay elementos en la lista")

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

    def length (self):
        if self.prim != None:
            count = 0
            nodo = self.prim
            while nodo:
                count += 1
                nodo = nodo.prox
            else:
                count += 1
                return count