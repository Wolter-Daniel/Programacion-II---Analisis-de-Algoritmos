'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

'''
Realice un programa que solicite al usuario el nombre completo de la persona, 
el DNI de la persona, la edad de la persona y la altura de la persona. Luego el 
programa debe mostrar por pantalla dos líneas de texto por separado: 
    a. En una línea imprimir el nombre completo y el DNI, aclarando de que 
    campo se trata cada uno. Por ej.: Nombre Completo: Elena Lobo, DNI: 
    38041532. 

    b. En la segunda línea se debe imprimir el nombre completo, edad y altura 
    de la persona. Nuevamente debe aclarar el campo de cada uno, para el 
    que lo lea entienda de que se está hablando. 
'''

class TP2_Ejercio_13 ():
    def main():
        nombre = input("Ingrese su nombre y apellido: ")
        dni = int(input("Ingrese su DNI: "))
        edad = int(input("Ingrese su edad: "))
        altura = float(input("Ingrese su altura: (ej: 1.97) "))

        texto_a = "Nombre completo: {}, DNI: {}".format(nombre, dni)
        texto_b = "Nombre completo: %s, edad: %d, altura: %s" %(nombre, edad, altura)

        print(texto_a)
        print(texto_b)

if __name__ == "__main__":
    TP2_Ejercio_13.main()