def juego_vidas():
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te queda 1 vida"
    yield "Game Over"

# Asegúrate de que esté escrito exactamente así, en singular y sin paréntesis:
perder_vida = juego_vidas()