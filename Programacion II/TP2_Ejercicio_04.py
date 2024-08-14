'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

#Solicitar al usuario el ingreso de su nombre, luego de su apellido (dos ingresos). 
#Luego mostrar por pantalla un mensaje de bienvenida completo. Por ej., si 
#ingresó Julián Alvarez: “¡¡Bienvenido Julián Alvarez!!” (utilizando una variable 
#para nombre y otra para apellido)

class TP2_Ejercio_04 ():
    def main():
        nombre = input("Ingrese su nombre:")
        apellido = input("Ingrese su apellido:")
        print("¡¡¡Bienvenido", nombre, apellido, "!!!")

if __name__ == "__main__":
    TP2_Ejercio_04.main()