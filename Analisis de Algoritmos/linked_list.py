'''
    Linked list nodo.
    Practica Analisis de Algoritmos Computacionales.
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''
class Nodo (object):

    #Constructor

    def __init__ (self, dato = None, prox = None ):
        self.dato = dato
        self.prox = prox

    def verLista (nodo):
        while nodo:
            print(nodo.dato)
            nodo = nodo.prox

class Linked_list (object):
    def __init__ (self):
        self.prim = None

    # Método para agregar elementos en el frente de la linked list

    def add_at_front (self, data):
        self.prim = Nodo(dato = data, prox = self.prim)

    # Metodo para agregar elementos al final de la lista

    def add_at_end (self, data):
        if self.prim == None:
            self.add_at_front(data)
            return
        else:
            nodo = self.prim
            while nodo.prox:
                nodo = nodo.prox
            else:
                nodo.prox = Nodo(data) 

    #Metodo para buscar elemento

    def search_data (self, data):
        nodo = self.prim
        while nodo.prox:
            if nodo.dato == data:
                return nodo
            else:
                nodo = nodo.prox
        else:
            print("Dato no existente") 

    #Metodo para eliminar un dato

    def delete_nodo (self, data):
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

    # Método para verificar si la estructura de datos esta vacia

    def is_empty (self):
        empety = "True" if self.prim == None else "False"
        print(empety)
    
    # Metodo para mostrar lista.
    
    def print_list (self):
        nodo = self.prim
        while nodo != None :
            print("Dato:", nodo.dato, "prox:", nodo.prox)
            nodo = nodo.prox

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

#linked_list.is_empty()

linked_list.delete_nodo("Hola")

linked_list.print_list()