'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

#Solicitar al usuario el ingreso de dos palabras y armar combinaciones con ellas. 
#De la primera palabra tome las primeras tres letras, utilice el operador “:”. De la 
#segunda palabra tome las primeras dos letras, utilice el operador “:”. Formar una 
#nueva palabra con los recortes solicitados y mostrarlo por pantalla.

class TP2_Ejercio_11 ():
    def main():
        print("Combinaremos palabras :)")
        texto1 = input("Ingrese una palabra: ")
        texto2 = input("Ingrese la segunda palabra: ")
        combinacion = texto1[0:3] + texto2[0:2]
        print("La nueva palabra es: ",combinacion)

if __name__ == "__main__":
    TP2_Ejercio_11.main()