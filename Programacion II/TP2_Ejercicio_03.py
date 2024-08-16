'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

#Solicitar al usuario el ingreso de dos números enteros. Calcular (utilizando 
#distintas variables), su suma, resta, multiplicación y división. Mostrar por 
#pantalla el resultado de cada una de las operaciones realizadas. Por ej. si el 
#usuario ingresó 4 y 7. Mostrar “El resultado de multiplicar 4 x 7 es 28”.

class TP2_Ejercio_03 ():
    def main():
        print("Calculadora basica")
        num1 = int(input("Ingrese un numero entero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        suma = num1 + num2
        resta = num1 - num2
        producto = num1 * num2
    
        if num2 == 0:
            print("No es posible la division por 0")
        else:
            division = num1 / num2
            print ("La division de", num1, "/", num2, "=", division)
        
        print ("La suma de", num1, "+", num2, "=", suma)
        print ("La resta de", num1, "-", num2, "=", resta)
        print ("El producto de", num1, "*", num2, "=", producto)

if __name__ == "__main__":
    TP2_Ejercio_03.main()