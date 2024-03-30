import pygame
import random
import os
import sys


pygame.init()

hit_sound = pygame.mixer.Sound('sound/target catch.mp3')  # sound for hitting target
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snitch in Moscow")
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)


# Load Cursor Image
cursor_image = pygame.image.load("img/harry.png").convert_alpha()

# Scale the cursor image to match the required dimensions
cursor_image = pygame.transform.scale(cursor_image, (80, 60))

# Set Cursor
pygame.mouse.set_visible(False)  # Hide the system cursor
cursor_rect = cursor_image.get_rect()






target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Variables for controlling the target's movement
target_speed = 1
target_direction_x = random.choice([-1, 1])
target_direction_y = random.choice([-1, 1])

#color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) background taking whatever unified color

# Load background images
background_images_dir = 'background'
background_images = [pygame.image.load(os.path.join(background_images_dir, filename)) for filename in os.listdir(background_images_dir)]#joins the directory with each filename for each file listed in the directory

# Select a random background image
background = random.choice(background_images)

# Scale background image to fit the screen
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load font
font = pygame.font.Font(None, 36)

running = True

clock = pygame.time.Clock()
points = 0

while running:
    #screen.fill(color)
    screen.blit(background, (0, 0))  # Draw the background image at coordinate (0,0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                points += 1
                hit_sound.play()

    # Get mouse position
    mouse_position = pygame.mouse.get_pos()

    # Set the position of the cursor image
    cursor_rect.center = mouse_position

    # Blit the cursor image at the mouse position
    screen.blit(cursor_image, cursor_rect)

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
    #pygame.display.update()
    # Update the display
    pygame.display.flip()

    clock.tick(60)  # Limit frame rate to 60 FPS


pygame.quit()
sys.exit()