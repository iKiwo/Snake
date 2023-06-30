import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
width = 800
height = 600

# Color gris medio oscuro
bg_color = (50, 50, 50)

# Tamaño del bloque de la serpiente y velocidad de movimiento
snake_block_size = 20
snake_speed = 15

# Tamaño del bloque de la manzana
apple_block_size = 20

# Colores
snake_color = (0, 255, 0)
apple_color = (255, 0, 0)

# Crear la ventana
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, snake_color, [x, y, snake_block_size, snake_block_size])


def draw_apple(apple_pos):
    pygame.draw.rect(window, apple_color, [apple_pos[0], apple_pos[1], apple_block_size, apple_block_size])


def generate_apple():
    apple_x = random.randint(0, (width - apple_block_size) // snake_block_size) * snake_block_size
    apple_y = random.randint(0, (height - apple_block_size) // snake_block_size) * snake_block_size
    return apple_x, apple_y


def show_score(score):
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))


def game_loop():
    # Coordenadas iniciales de la serpiente
    x1 = width / 2
    y1 = height / 2

    # Cambios en las coordenadas de la serpiente
    x1_change = 0
    y1_change = 0

    # Cuerpo de la serpiente
    snake_list = []
    length_of_snake = 1

    # Posición inicial de la manzana
    apple_pos = generate_apple()

    game_over = False
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Actualizar las coordenadas de la serpiente
        x1 += x1_change
        y1 += y1_change

        # Verificar si la serpiente sale de los límites de la ventana
        if x1 >= width:
            x1 = 0
        elif x1 < 0:
            x1 = width - snake_block_size
        elif y1 >= height:
            y1 = 0
        elif y1 < 0:
            y1 = height - snake_block_size

        # Verificar colisión con el cuerpo de la serpiente
        snake_head = [x1, y1]
        if snake_head in snake_list[:-1]:
            game_over = False

        # Agregar las coordenadas de la cabeza de la serpiente al cuerpo
        snake_list.append(snake_head)

        # Mantener el tamaño del cuerpo de la serpiente
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Verificar colisión con la manzana
        if x1 == apple_pos[0] and y1 == apple_pos[1]:
            apple_pos = generate_apple()
            length_of_snake += 1
            score += 1

        # Actualizar la ventana
        window.fill(bg_color)
        draw_snake(snake_list)
        draw_apple(apple_pos)
        show_score(score)
        pygame.display.update()

        # Limitar la velocidad de actualización del juego
        clock.tick(snake_speed)

    # Finalizar Pygame
    pygame.quit()


# Iniciar el juego
game_loop()
