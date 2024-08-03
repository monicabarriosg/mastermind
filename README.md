# Mi Proyecto Python
## Estructura del Proyecto

- `game.py`: Control del juego.
- `player.py`: Clase para el jugador adivinador.
- `code_creator.py`: Clase para el creador del código.
- `board.py`: Clase para el tablero.


## Clases Básicas

### Clase `Juego` (`game.py`)

- **`__init__()`**: lo que va a hacer es inicializar el juego con un codificador, un jugador, y un tablero.
- **`iniciar_juego()`**: Maneja el flujo principal del juego, permite al jugador hacer intentos y verifica si alguno ha ganado.
- **`verificar_ganador(adivinanza)`**: Verifica si la adivinanza del jugador coincide con el código secreto del codificador.

### Clase `Jugador` (`player.py`)

- **`__init__(name)`**: Inicializa al jugador con un nombre.
- **`adivinar_codigo()`**: Permite al jugador adivinar el código introduciendo una lista de colores con una serie de colores especificos
