class Juego():

    def __init__(self):
        self.turn = 0 # si turno es par le toca al jugador, caso contrario a la compu 

    def combate(self, participante1, participante2):
        if participante1.velocidad < participante2.velocidad: self.turn = 1

        while True:
            if self.turn % 2 == 0:
                participante1.eleccion()
            
        

    def eleccion(self):

        self.mostrar_menu()

        eleccion = int(input("Elije tu siguiente movimiento: "))

        while(eleccion > 4 or eleccion < 1):
            print("Eleccion incorrecta, por favor elige")

            self.mostrar_menu()
        
            eleccion = int(input("Elije tu siguiente movimiento: "))

        