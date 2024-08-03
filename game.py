import random
from player import Player
from code_creator import code_creator
from board import Board

class Juego:
    def __init__(self):
        self.code_creator = code_creator()
        self.board = Board()
        self.player = Player("Jugador Adivinador")
        self.intentos_hechos = 0
        self.intentos_maximos = 10
        

    def inicio_juego(self):
        self.code_creator.generate_code()
        print("inicio")
        print("creo codigo secreto")
        while self.intentos_hechos < self.intentos_maximos:
            print(f"Intento {self.intentos_hechos + 1}/{self.intentos_maximos}")
            adivinanza = self.player.adivinar_codigo()
            if self.verifica_ganador(adivinanza):
                print("bien")
                break
            self.intentos_hechos += 1
            self.board.display()  
        else:
            print(f"mal. El código era: {self.code_creator.code}")

    def verifica_ganador(self, adivinanza):
        return adivinanza == self.code_creator.code
