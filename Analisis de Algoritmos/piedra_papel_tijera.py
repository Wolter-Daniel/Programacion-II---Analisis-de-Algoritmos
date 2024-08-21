'''
    Analisis de algoritmos
    UCASAL. Lic.Ciencia de Datos.
    Alumno: Daniel Andres Wolter.
'''

'''
Desarrollar un algoritmo que permita a dos jugadores participar en el juego "Piedra, Papel o Tijera". El algoritmo debe cumplir con los siguientes requisitos:

Entradas del Juego:

Los jugadores deben introducir sus elecciones de manera simultánea. Las opciones posibles son: "Piedra", "Papel" o "Tijera".
Validar que las entradas sean correctas. Si alguna entrada no es válida, solicitar nuevamente la elección del jugador.
Reglas del Juego:

Piedra vence a Tijera.
Tijera vence a Papel.
Papel vence a Piedra.
Si ambos jugadores eligen la misma opción, es un empate.
Salida del Juego:

Determinar el ganador según las reglas del juego.
Mostrar el resultado del juego indicando cuál jugador ganó, o si fue un empate.
Repetición del Juego:

Preguntar a los jugadores si desean jugar nuevamente.
Si la respuesta es afirmativa, reiniciar el juego.
Si la respuesta es negativa, terminar el programa.
'''

class piedra_papel_tijera ():
    def main():
        print("Jugaremos a Piedra, Papel o tijera")
        piedra_papel_tijera.game()
        
    def game():
        count_1 = 0
        count_2 = 0
        jugador_1 = 0
        jugador_2 = 0
        for i in range(3):
            print("Ronda ", i+1)
            while jugador_1 >3 or jugador_1 < 1:
                print("Jugador 1 seleccione una opcion: ")
                jugador_1 = int(input("1) Piedra, 2) Papel, 3)Tijera "))
                if jugador_1 >3 or jugador_1 < 1:
                    print("Seleccion invalida, Intente de nuevo!")
            while jugador_2 >3 or jugador_2 < 1:
                print("Jugador 2 seleccione una opcion: ")
                jugador_2 = int(input("1) Piedra, 2) Papel, 3)Tijera "))
                if jugador_2 >3 or jugador_2 < 1:
                    print("Seleccion invalida, Intente de nuevo!")

            if jugador_1 == 1 and jugador_2 == 3:
                count_1 += 1
            elif jugador_1 == 1 and jugador_2 == 2:
                count_2 += 1
            elif jugador_1 == 2 and jugador_2 == 1:
                count_1 += 1
            elif jugador_1 == 2 and jugador_2 == 3:
                count_2 += 1
            elif jugador_1 == 3 and jugador_2 == 2:
                count_1 += 1
            elif jugador_1 == 3 and jugador_2 == 1:
                count_2 += 1

            jugador_1 = 0
            jugador_2 = 0

        if count_1 > count_2:
            print("Jugador 1 es el ganador!!!")
        elif count_1 < count_2:
            print("Jugador 2 es el ganador!!!")
        else:
            print("Es un empate!!!")

        print("Si desea volver a jugar ingrese SI por consola")
        print("Si desea salir presione enter")
        repeat = input()
        if repeat == "SI":
            piedra_papel_tijera.game()
        else:
            return



if __name__ == "__main__":
    piedra_papel_tijera.main()