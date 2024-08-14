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
        operador = input("Ingrese la operacion a realizar (+, -, * , /): ")
        num2 = int(input("Ingrese el segundo numero: "))
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                print("No es posible la division por 0")
                return
            else:
                resultado = num1 / num2
        else:
            print("El operador no es valido :(")
            return
        
        print (num1, operador, num2, "=", resultado)
        return

if __name__ == "__main__":
    TP2_Ejercio_03.main()