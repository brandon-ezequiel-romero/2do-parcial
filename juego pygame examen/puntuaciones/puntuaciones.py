import os
import pygame
# Ruta del archivo de puntuaciones
archivo_puntuaciones = "juego pygame examen/puntuaciones/puntuaciones.txt"

# Verificar si el archivo de puntuaciones existe
def verificar_archivo():
    if not os.path.exists(archivo_puntuaciones):
        with open(archivo_puntuaciones, 'w') as archivo:
            archivo.write("Nombre,Puntuación\n")  # Escribimos una línea de cabecera si el archivo no existe

# Función para guardar la puntuación
def guardar_puntuacion(nombre, puntuacion):
    verificar_archivo()  # Aseguramos que el archivo exista

    # Abrimos el archivo en modo 'a' para agregar nuevas puntuaciones
    with open(archivo_puntuaciones, 'a') as archivo:
        archivo.write(f"{nombre},{puntuacion}\n")  # Escribimos el nombre y la puntuación

# Función para mostrar las puntuaciones
def mostrar_puntuaciones(pantalla):
    verificar_archivo()  # Aseguramos que el archivo exista

    fuente = pygame.font.Font(None, 36)
    pantalla.fill((0, 0, 0))

    # Leemos las puntuaciones del archivo
    with open(archivo_puntuaciones, 'r') as archivo:
        lineas = archivo.readlines()

    # Mostrar puntuaciones en pantalla
    y_offset = 50
    for linea in lineas[1:]:  # Omitir la cabecera
        nombre, puntuacion = linea.strip().split(',')
        texto = fuente.render(f"{nombre}: {puntuacion}", True, (255, 255, 255))
        pantalla.blit(texto, (50, y_offset))
        y_offset += 40  # Espaciado entre las puntuaciones

    pygame.display.flip()
    pygame.time.wait(5000)  # Mostrar las puntuaciones durante 5 segundos
