from colored import fore, style

class Board:
    def __init__(self):
        self.moves = []
        self.devolver_retroalimentacion = []

    def actualizar_tablero(self, adivinanza, retroalimentacion):
        self.moves.append(adivinanza)
        self.devolver_retroalimentacion.append(retroalimentacion)

    def mostrar(self):
        red = fore('red')
        green = fore('green')
        reset = style('reset')
        print("\nTablero:")
        for move, feedback in zip(self.moves, self.devolver_retroalimentacion):
          print(f"{green}Adivinanza: {move}{reset}")
          print(f"{red}Retroalimentación: {feedback}{reset}")
            # print("Adivinanza: ", move)
            # print("Retroalimentación: ", devolver_retroalimentacion)