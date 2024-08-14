'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

#Solicitar al usuario el ingreso de 3 palabras y armar un acrónimo con ellas. De 
#cada palabra debe tomar la primera letra y armar el acrónimo. Ejemplo: Qatar, 
#Argentina y Mundial --> QAM. Mostrar el resultado por pantalla. 

class TP2_Ejercio_09 ():
    def main():
        print("Crearemos un acronimo")
        text1 = input("Ingrese la primer palabra: ")
        text2 = input("Ingrese la segunda palabra: ")
        text3 = input("Ingrese la tercer palabra: ")
        acronimo = text1[0] + text2[0] + text3[0]
        print("El acronimo de", text1, ",", text2, ",", text3, "es:", acronimo)

if __name__ == "__main__":
    TP2_Ejercio_09.main()