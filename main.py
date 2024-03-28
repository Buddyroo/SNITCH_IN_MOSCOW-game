import pygame

pygame.init()#инициализация библиотеки

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dart Game")
icon = pygame.image.load('icon.png')

running = True

while running:
    pass

pygame.quit()

