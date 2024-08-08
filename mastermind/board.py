from colored import fore, style
#clase para el tablero
class Board:
    #inicializa 
    def __init__(self):
        self.intentos = []
    #actualiza el tablero para dar retroalimentacion
    def actualizar_tablero(self, intento, retroalimentacion):
        self.intentos.append((intento, retroalimentacion))
    #funcion para mostar la retroalimentacion
    def mostrar(self):
        print(f"{fore.CYAN}Tablero de Intentos:{style.RESET}")
        for intento, retroalimentacion in self.intentos:
            intento_display = ' '.join(intento)
            retroalimentacion_display = ' '.join(retroalimentacion)
            print(f"Intento: {intento_display} | Retroalimentación: {retroalimentacion_display}")
