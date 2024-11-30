import pygame
from menu.menu import mostrar_menu
from juego.juego import jugar
from puntuaciones.puntuaciones import mostrar_puntuaciones

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("star wars(enzo te amo por fa apruebame)")

    # Cargar y reproducir música
    pygame.mixer.music.load("juego pygame examen/assets/musica_fondo.wav")
    pygame.mixer.music.set_volume(0.5)  # Volumen al 50%
    pygame.mixer.music.play(-1)  # Repetir infinitamente

    corriendo = True
    while corriendo:
        opcion = mostrar_menu(pantalla)
        if opcion == 0:  # Jugar
            jugar(pantalla)
        elif opcion == 1:  # Ver puntuaciones
            mostrar_puntuaciones(pantalla)
        elif opcion == 2:  # Salir
            corriendo = False

    pygame.quit()

if __name__ == "__main__":
    main()
