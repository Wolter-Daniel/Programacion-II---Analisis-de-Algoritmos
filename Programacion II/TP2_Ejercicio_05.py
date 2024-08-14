'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

#Ídem ejercicio 4 pero una vez ingresados nombres y apellidos, almacenarlos en 
#una sola variable y mostrar el mensaje de bienvenida. 


class TP2_Ejercio_05 ():
    def main():
        nombre = input("Ingrese su nombre:")
        apellido = input("Ingrese su apellido:")
        nombre_completo = nombre + " " + apellido
        print("¡¡¡Bienvenido", nombre_completo, "!!!")

if __name__ == "__main__":
    TP2_Ejercio_05.main()