'''Linked list nodo.
    Practica Analisis de Algoritmos Computacionales.
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''
class Nodo (Int):
    def __init__(self, dato = None, prox = None ):

        #Constructor
        
        self.dato = dato
        self.prox = prox