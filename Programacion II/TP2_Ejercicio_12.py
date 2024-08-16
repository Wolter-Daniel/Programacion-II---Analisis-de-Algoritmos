'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

#Realice una calculadora, el usuario ingresará dos números reales y se deberán 
#calcular todas las operaciones entre ellos: A) Suma; B) Resta; C) Multiplicación; 
#D) División; E) Exponente/Potencia. Para todos los casos se debe imprimir en 
#pantalla el resultado aclarando la operación realizada en cada caso y con que 
#números se ha realizado la operación. Por ej: “La suma entre 14.1 y 6.4 es 20.5”

class TP2_Ejercio_12 ():
    def main():
        print("Calculadora basica")
        num1 = int(input("Ingrese un numero entero: "))
        operador = input("Ingrese la operacion a realizar (+, -, * , /, ** #Potencia): ")
        num2 = int(input("Ingrese el segundo numero: "))
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "**":
            resultado = num1 ** num2
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
    TP2_Ejercio_12.main()