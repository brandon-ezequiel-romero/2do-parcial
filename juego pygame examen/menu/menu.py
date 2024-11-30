import pygame

def mostrar_menu(pantalla):
    opciones = ["Jugar", "Ver Puntuaciones", "Salir"]
    fuente = pygame.font.Font(None, 50)
    seleccion = 0

    while True:
        pantalla.fill((0, 0, 0))

        for i, opcion in enumerate(opciones):
            color = (255, 255, 255) if i == seleccion else (100, 100, 100)
            texto = fuente.render(opcion, True, color)
            pantalla.blit(texto, (300, 200 + i * 60))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 2  # Salir
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    return seleccion
