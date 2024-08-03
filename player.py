class Player:
    def __init__(self, name):
        self.name = name

    def adivinar_codigo(self):
        colores = ["rojo", "azul", "verde", "amarillo"]
        print("tu codigo secreto:")
        print(", ".join(colores))
        adivinanza = input("Tu adivinanza: ").strip().lower().split(',')
        adivinanza = [color.strip() for color in adivinanza]
        if len(adivinanza) != 4 or not all(color in colores for color in adivinanza):
            print("no.")
            return self.adivinar_codigo()
        return adivinanza
