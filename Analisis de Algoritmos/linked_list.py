'''
    Linked list.
    Practica Analisis de Algoritmos Computacionales.
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''
class Nodo (object):

    #Constructor

    def __init__ (self, dato = None, prox = None ):
        self.dato = dato
        self.prox = prox

class Linked_list (object):
    '''Craer un objeto de tipo lista enlazada'''
    def __init__ (self):
        self.prim = None


    def add_at_front (self, data):
        '''Método para agregar elementos en el frente de la linked list'''
        self.prim = Nodo(dato = data, prox = self.prim)


    def add_at_end (self, data):
        '''Metodo para agregar elementos al final de la lista'''
        if self.prim == None:
            self.add_at_front(data)
            return
        else:
            nodo = self.prim
            while nodo.prox:
                nodo = nodo.prox
            else:
                nodo.prox = Nodo(data) 


    def search_data (self, data):
        '''Metodo para buscar elemento'''
        nodo = self.prim
        while nodo.prox:
            if nodo.dato == data:
                return nodo
            else:
                nodo = nodo.prox
        else:
            print("Dato no existente") 


    def delete_nodo (self, data):
        '''Metodo para eliminar un dato'''
        nodo = self.prim
        prev = None
        while nodo.prox:
            if nodo.dato == data and prev == None:
                self.prim = nodo.prox
                return
            elif nodo.dato != data:
                prev = nodo
                nodo = nodo.prox
            else:
                prev.prox = nodo.prox
                return
        else:
            print("Dato no existente")


    def is_empty (self):
        '''Método para verificar si la estructura de datos esta vacia'''
        empty = "True" if self.prim == None else "False"
        return empty
    

    def print_list (self):
        '''Metodo para mostrar lista.'''
        nodo = self.prim
        while nodo != None :
            print("Dato:", nodo.dato, "prox:", nodo.prox)
            nodo = nodo.prox
    

    def length (self):
        '''Metodo para obtener cantidad de elementos'''
        nodo = self.prim
        if self.is_empty() == "False":
            count = 0
            while nodo.prox:
                count += 1
                nodo = nodo.prox
            else:
                count += 1
            return count
        else:
            print("Lista vacia")

v3 = Nodo ("Manzanas")
v2 = Nodo ("Peras", v3)
v1 = Nodo ("Bananas", v2)

#Referencia del principio de la lista.

lista = v1 

#print(v1.dato)
#print(v2.dato)
#print(v3.dato)

#_Nodo.verLista(lista)

linked_list = Linked_list()
linked_list.add_at_end("Hola")
linked_list.add_at_end("Mundo")
linked_list.add_at_end("!")
linked_list.add_at_end("!")
linked_list.add_at_end("!")
linked_list.add_at_front("#")
linked_list.print_list()
print(linked_list.length())
#linked_list.is_empty()
#linked_list.delete_nodo("Hola")
#linked_list.print_list()
