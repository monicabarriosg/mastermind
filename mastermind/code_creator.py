import random
#clase  para creacion del codigo de manera aleatoria
class CodeMaker:
    def __init__(self):
        self.code = None

    def establecer_codigo(self):
        while True:
            codigo = input("Introduce el código secreto (4 caracteres, por ejemplo 'RGBYr'): ").strip().upper()
            if len(codigo) == 4 and codigo.isalpha():
                self.code = codigo
                break
            else:
                print("Código inválido. Debe tener 4 caracteres alfabéticos.")

    def generar_codigo_aleatorio(self):
        colores = ['R', 'G', 'B', 'Y', 'O', 'P']  
        self.code = ''.join(random.choice(colores) for _ in range(4))
        print(f"El código secreto generado es: {self.code}")
        return self.code
