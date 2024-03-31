# Import necessary libraries
import pygame
import random
import os
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function to display welcome message
def display_welcome_message():
    # Load font for the welcome message
    welcome_font = pygame.font.Font(None, 36)

    # Render the welcome message
    welcome_text_line1 = welcome_font.render("Добро пожаловать на квиддич-чемпионат в Москве!", True, WHITE)
    welcome_text_line2 = welcome_font.render("Приготовьте свою метлу, мы начинаем...", True, WHITE)

    # Get the rectangles for the welcome message texts
    welcome_rect_line1 = welcome_text_line1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
    welcome_rect_line2 = welcome_text_line2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))

    # Create a rectangle slightly larger than the text for the background
    background_rect = pygame.Rect(welcome_rect_line1.left - 20, welcome_rect_line1.top - 20,
                                  welcome_rect_line1.width + 40,
                                  welcome_rect_line1.height + welcome_rect_line2.height + 80)

    # Draw the black rectangle background
    pygame.draw.rect(screen, BLACK, background_rect)

    # Draw the welcome message on the screen
    screen.blit(welcome_text_line1, welcome_rect_line1)
    screen.blit(welcome_text_line2, welcome_rect_line2)

    # Update the display
    pygame.display.flip()

    # Wait for 5 seconds
    pygame.time.delay(5000)

# Load sound for hitting target
hit_sound = pygame.mixer.Sound('sound/target catch.mp3')

# Create display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snitch in Moscow")
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

# Load Cursor Image
cursor_image = pygame.image.load("img/harry.png").convert_alpha()
cursor_image = pygame.transform.scale(cursor_image, (80, 60))

# Set Cursor
pygame.mouse.set_visible(False)
cursor_rect = cursor_image.get_rect()

# Timer variables
start_time = pygame.time.get_ticks()
total_time = 10000

# Load target image
target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

# Variables for controlling the target's movement
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed = 1
target_direction_x = random.choice([-1, 1])
target_direction_y = random.choice([-1, 1])

# Define levels
levels = [{"duration": 10000} for _ in range(10)]

# Load target GIF animation frames
target_animation_frames = [pygame.image.load(f"animation hit target/frame_{i}.gif").convert_alpha() for i in range(1, 45)]

# Load background images
background_images_dir = 'background'
background_images = [pygame.image.load(os.path.join(background_images_dir, filename)) for filename in os.listdir(background_images_dir)]
background = random.choice(background_images)
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load font
font = pygame.font.Font(None, 36)

# Main loop
running = True
level = 0
clock = pygame.time.Clock()
welcome_displayed = False
points = 0
play_target_animation = False
animation_index = 0
animation_duration = 500
animation_timer = 0

while running:
    screen.blit(background, (0, 0))
    if not welcome_displayed:
        display_welcome_message()
        welcome_displayed = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                points += 1
                hit_sound.play()
                play_target_animation = True
                animation_timer = pygame.time.get_ticks()

    current_time = pygame.time.get_ticks()
    time_left = max(levels[level]["duration"] - (current_time - start_time), 0) // 1000
    timer_text = font.render("Time left: " + str(time_left), True, WHITE)
    screen.blit(timer_text, (10, 50))

    mouse_position = pygame.mouse.get_pos()
    cursor_rect.center = mouse_position
    screen.blit(cursor_image, cursor_rect)

    target_x += target_speed * target_direction_x
    target_y += target_speed * target_direction_y

    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_direction_x *= -1
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_direction_y *= -1

    points_text = font.render("Points: " + str(points), True, WHITE)
    screen.blit(points_text, (10, 10))
    screen.blit(target_img, (target_x, target_y))

    if play_target_animation:
        if current_time - animation_timer < animation_duration:
            screen.blit(target_animation_frames[animation_index], (target_x, target_y))
        else:
            play_target_animation = False
        animation_index = (animation_index + 1) % len(target_animation_frames)
    else:
        screen.blit(target_img, (target_x, target_y))

    if time_left == 0:
        action = show_popup("Время вышло. Потренируйтесь летать на метле и возвращайтесь!")
        if action == "retry":
            start_time = pygame.time.get_ticks()
            points = 0
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        elif action == "exit":
            pygame.quit()
            sys.exit()

    if points >= 5:
        level += 1
        if level < len(levels):
            target_speed += 1
            background = random.choice(background_images)
            screen.blit(background, (0, 0))
            pygame.display.flip()
            pygame.time.wait(500)
            start_time = pygame.time.get_ticks()
            points = 0
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        else:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()