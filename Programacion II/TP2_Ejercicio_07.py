'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

#Solicitar al usuario el ingreso de una palabra cualquiera, y mostrarle por pantalla 
#cuántas letras tiene la palabra ingresada.

class TP2_Ejercio_07 ():
    def main():
        print("Contador de caracteres!!!")
        texto = input("Ingrese una palabra: ")
        print("La cantidad de letras de la palabra", texto,"es:", len(texto)) 

if __name__ == "__main__":
    TP2_Ejercio_07.main()