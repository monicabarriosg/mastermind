import random
class Code_creator:
    def __init__(self):
        self.code = []

    def establecer_codigo(self):
        colores = ["rojo", "azul", "verde", "amarillo"]
        print("Introduce el código secreto usando los colores:")
        print(", ".join(colores))
        codigo = input("Código secreto: ").strip().lower().split(',')
        codigo = [color.strip() for color in codigo]
        if len(codigo) != 4 or not all(color in colores for color in codigo):
            print("Entrada inválida. Asegúrate de usar solo los colores permitidos y.")
            return self.establecer_codigo()
        self.code = codigo

    def generar_codigo_aleatorio(self):
        colores = ["rojo", "azul", "verde", "amarillo"]
        self.code = [random.choice(colores) for _ in range(4)]
