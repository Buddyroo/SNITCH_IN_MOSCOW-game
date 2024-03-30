import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Target Game")
icon = pygame.image.load('img/download.jpeg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Variables for controlling the target's movement
target_speed = 2
target_direction_x = random.choice([-1, 1])
target_direction_y = random.choice([-1, 1])

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Load font
font = pygame.font.Font(None, 36)

running = True

clock = pygame.time.Clock()
points = 0

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                points += 1

    # Update target's position
    target_x += target_speed * target_direction_x
    target_y += target_speed * target_direction_y

    # Bounce target off the edges
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_direction_x *= -1
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_direction_y *= -1

        # Render points as text
    points_text = font.render("Points: " + str(points), True, (255, 255, 255))

    # Blit points text onto the screen at position (10, 10)
    screen.blit(points_text, (10, 10))
    #blits the target image onto the screen
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

    clock.tick(60)  # Limit frame rate to 60 FPS


pygame.quit()