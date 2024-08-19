'''
    Trabajo Practico 2
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

'''
- Realice un programa que determine cual sería el apellido de una persona al 
ingresar los dos nombres completos de sus padres. Es decir, se solicita crear una 
variable nueva que reúna los apellidos. Primero el programa debe consultar el 
nombre completo del padre_1, luego el programa debe consultar el nombre 
completo del padre_2, luego debe consultar el nombre del hijo/a. Debe extraer 
los apellidos de los padres (ver la nota al final). Luego formar el nombre completo 
del hijo/a utilizando los apellidos de sus padres y el nombre ingresado de dicha 
persona. Mostrar por pantalla el resultado. 
    NOTA: Para extraer el apellido del nombre completo recomiendo usar el 
    método "split". Por ejemplo: 
    *$direccion_completa = 'Mitre 465' 
    *$calle, altura = direccion_completa.split(' ')
'''

class TP2_Ejercio_15 ():
    def main():
        padre_1 = input("Ingrese el nombre completo del primer padre:")
        padre_2 = input("Ingrese el nombre completo del segundo padre:")
        hijo = input("Ingrese el nombre completo del hijo: ")
        nombre_padre_01, apellido_padre_1 = padre_1.split(" ")
        nombre_padre_02, apellido_padre_2 = padre_2.split(" ")
        hijo = hijo + " " + apellido_padre_1 + " " + apellido_padre_2
        print("El nombre completo del hijo es: ", hijo)

if __name__ == "__main__":
    TP2_Ejercio_15.main()