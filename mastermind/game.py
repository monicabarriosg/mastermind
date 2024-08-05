# import random
from player import Player
from colored import fore, style

from code_creator import Code_creator
from board import Board


class Juego:
    def __init__(self):
        self.code_creator = Code_creator()
        self.board = Board()
        self.player = Player("Jugador Adivinador")
        self.intentos_hechos = 0
        self.intentos_maximos = 10
        self.code_creator.generar_codigo_aleatorio()
        
    def inicio_juego(self):
        # self.code_creator.generate_code()
        print("El juego ha comenzado.")
        print("¿Eres el creador del código o el adivinador?")
        rol = input("Escribe 'creador' para ser el creador del código o 'adivinador' para adivinar: ").strip().lower()
        if rol == 'creador':
            self.code_creator.establecer_codigo()
        else:
            self.code_creator.generar_codigo_aleatorio()
            print("El codificador ha creado un código secreto.")
        
        while self.intentos_hechos < self.intentos_maximos:
            print(f"Intento {self.intentos_hechos + 1}/{self.intentos_maximos}")
            adivinanza = self.player.adivinar_codigo()
            retroalimentacion = self.obtener_retroalimentacion(adivinanza) 
            self.board.actualizar_tablero(adivinanza, retroalimentacion)
            if self.verifica_ganador(adivinanza):
                print("bien")
                break
            self.intentos_hechos += 1
            self.board.display()  
        else:
            print(f"mal. El código era: {self.code_creator.code}")

    def verifica_ganador(self, adivinanza):
        return adivinanza == self.code_creator.code
    def obtener_retroalimentacion(self, adivinanza):
        colores = {  
        "rojo": fore.RED,
        "azul": fore.BLUE,
        "verde": fore.GREEN,
        "amarillo": fore.YELLOW,
        "blanco": fore.WHITE
        }  
        get_feedback = []
        for i in range(4):
            if adivinanza[i] == self.code_creator.code[i]:
                get_feedback.append(fore.RED + adivinanza[i].upper() + style.RESET) 
            elif adivinanza[i] in self.code_creator.code:
                get_feedback.append(fore.YELLOW + adivinanza[i].upper() + style.RESET)
            else:
                get_feedback.append(fore.WHITE + adivinanza[i].upper() + style.RESET)  
        return get_feedback
    
