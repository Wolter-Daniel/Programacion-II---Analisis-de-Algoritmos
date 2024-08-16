'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

'''
Realice un programa que solicite al usuario el ingreso de un nombre completo. 
Luego lo muestre por pantalla en los siguientes formatos: 
    a. Todas las letras en minúsculas 
    b. Todas las letras en mayúsculas 
    c. Solo la primera letra del nombre en mayúscula
'''

class TP2_Ejercio_14 ():
    def main():
        nombre = input("Ingrese su nombre completo: ")
        print("Nombre en minuscula: ", nombre.lower() )
        print("Nombre en mayuscula: ", nombre.upper())
        print("Solo la primera letra del nombre en mayúscula: ", nombre.capitalize() )

if __name__ == "__main__":
    TP2_Ejercio_14.main()