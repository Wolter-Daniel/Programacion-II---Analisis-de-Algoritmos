'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

#Solicitar al usuario el ingreso del total de alumnos del curso, luego la cantidad de 
#mujeres y la cantidad de varones. Calcular y mostrar el porcentaje de varones y 
#mujeres de la clase.

class TP2_Ejercio_ ():
    def main():
       print("Calcularemos el porcentaje de alumnos mujeres y varones")
       total = int(input("Ingrese el numero total de alumno: "))
       cant_mujeres = int(input("Ingrese la cantidad de alumnos mujeres: "))
       cant_varones = int(input("Ingrese la cantidad de alumnos varones: "))
       porcentaje_mujeres = (cant_mujeres/total) * 100
       porcentaje_varones = (cant_varones/total) * 100 
       print("El porcentaje es: ")
       print("Mujeres: %", porcentaje_mujeres)
       print("Varones: %", porcentaje_varones)

if __name__ == "__main__":
    TP2_Ejercio_.main()