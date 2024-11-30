import random
import pygame
from puntuaciones.puntuaciones import guardar_puntuacion

# Configuración de colores y dimensiones
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
ANCHO = 800
ALTO = 600

# Cargar la imagen de fondo
fondo = pygame.image.load("juego pygame examen/assets/espacio.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))  # Redimensionar el fondo para que se ajuste a la pantalla

def jugar(pantalla):
    pygame.init()
    reloj = pygame.time.Clock()

    # Pantalla de ingreso de nombre
    nombre = ingresar_nombre(pantalla)

    # Configuración de la nave del jugador
    nave_jugador = pygame.image.load("juego pygame examen/assets/prota.png")
    nave_jugador = pygame.transform.scale(nave_jugador, (50, 50))
    jugador_rect = nave_jugador.get_rect(center=(ANCHO // 2, ALTO - 60))

    # Configuración de los enemigos
    enemigo_img = pygame.image.load("juego pygame examen/assets/enemigo.png")
    enemigo_img = pygame.transform.scale(enemigo_img, (50, 50))
    enemigos = []

    # Proyectiles del jugador
    disparos = []

    # Puntos y estado del juego
    puntos = 0
    corriendo = True

    while corriendo:
        pantalla.fill(NEGRO)

        # Dibujar el fondo en cada ciclo del juego
        pantalla.blit(fondo, (0, 0))

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and jugador_rect.left > 0:
            jugador_rect.x -= 5
        if keys[pygame.K_RIGHT] and jugador_rect.right < ANCHO:
            jugador_rect.x += 5
        if keys[pygame.K_SPACE]:  # Disparo
            if len(disparos) < 99999999999:  # Limitar el número de disparos activos
                disparos.append(pygame.Rect(jugador_rect.centerx - 2, jugador_rect.top - 10, 5, 10))

        # Movimiento de los disparos
        for disparo in disparos[:]:
            disparo.y -= 10
            if disparo.bottom < 0:
                disparos.remove(disparo)

        # Generar enemigos
        if random.randint(1, 1) == 1:  
            enemigos.append(pygame.Rect(random.randint(0, ANCHO - 50), -50, 50, 50))

        # Movimiento de los enemigos
        for enemigo in enemigos[:]:
            enemigo.y += 5
            if enemigo.top > ALTO:
                enemigos.remove(enemigo)

        # Detección de colisiones con disparos y eliminación de ambos
        for disparo in disparos[:]:
            for enemigo in enemigos[:]:
                if disparo.colliderect(enemigo):
                    disparos.remove(disparo)  # Eliminar el disparo que colisionó
                    enemigos.remove(enemigo)  # Eliminar el enemigo
                    puntos += 10
                    break  # Salir del loop interno para evitar errores

        # Detección de colisiones con el jugador
        for enemigo in enemigos:
            if jugador_rect.colliderect(enemigo):
                corriendo = False  # Fin del juego

        # Dibujar elementos en la pantalla (después de la imagen de fondo)
        pantalla.blit(nave_jugador, jugador_rect)
        for enemigo in enemigos:
            pantalla.blit(enemigo_img, enemigo)
        for disparo in disparos:
            pygame.draw.rect(pantalla, ROJO, disparo)

        # Mostrar puntos
        fuente = pygame.font.Font(None, 36)
        texto_puntos = fuente.render(f"Puntos: {puntos}", True, BLANCO)
        pantalla.blit(texto_puntos, (10, 10))

        pygame.display.flip()
        reloj.tick(30)

    # Guardar puntuación al finalizar
    guardar_puntuacion(nombre, puntos)

    # Mostrar mensaje de derrota
    mostrar_mensaje_derrota(pantalla, puntos)

def ingresar_nombre(pantalla):
    fuente = pygame.font.Font(None, 48)
    nombre = ""
    ingresando = True

    while ingresando:
        pantalla.fill(NEGRO)

        texto = fuente.render("Ingresa tu nombre: " + nombre, True, BLANCO)
        pantalla.blit(texto, (50, ALTO // 2))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre:
                    ingresando = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode

    return nombre

def mostrar_mensaje_derrota(pantalla, puntos):
    fuente = pygame.font.Font(None, 48)
    pantalla.fill(NEGRO)

    mensaje = (f"¡Perdiste! Puntos: {puntos}")
    texto = fuente.render(mensaje, True, ROJO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2))

    pygame.display.flip()
    pygame.time.wait(3000)
