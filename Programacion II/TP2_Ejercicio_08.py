'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

#Solicitar al usuario el ingreso de la BASE y la ALTURA de un triángulo, calcular y 
#mostrar el área del triángulo.

class TP2_Ejercio_08 ():
    def main():
        print("Calcularemos el area de un triangulo")
        base = int(input("Ingres el valor de la base: "))
        altura = int(input("Ingrese la altura del triangulo: "))
        resultado = (base * altura)/2
        print("El area del triangulo es:",resultado)

if __name__ == "__main__":
    TP2_Ejercio_08.main()