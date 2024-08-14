'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

#Solicitar al usuario el ingreso de dos números, calcular y mostrar el promedio de 
#ambos valores.

class TP2_Ejercio_06 ():
    def main():
        print("Calcularemos el promedio entre dos numeros")
        num1 = int(input("Ingrese un numero: "))
        num2 = int(input("Ingrese el segundo numero: "))

        print("El promedio es de: ", ((num1 + num2) / 2) )


if __name__ == "__main__":
    TP2_Ejercio_06.main()