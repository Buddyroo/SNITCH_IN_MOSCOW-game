import pygame
import random
import os
import sys


pygame.init()


# Function to display welcome message
def display_welcome_message():
    # Load font for the welcome message
    welcome_font = pygame.font.Font(None, 36)

    # Render the welcome message
    welcome_text_line1 = welcome_font.render("Добро пожаловать на квиддич-чемпионат в Москве!", True, (255, 255, 255))
    welcome_text_line2 = welcome_font.render("Приготовьте свою метлу, мы начинаем...", True, (255, 255, 255))

    # Get the rectangles for the welcome message texts
    welcome_rect_line1 = welcome_text_line1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
    welcome_rect_line2 = welcome_text_line2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))

    # Create a rectangle slightly larger than the text for the background
    background_rect = pygame.Rect(welcome_rect_line1.left - 20, welcome_rect_line1.top - 20,
                                  welcome_rect_line1.width + 40,
                                  welcome_rect_line1.height + welcome_rect_line2.height + 80)

    # Draw the black rectangle background
    pygame.draw.rect(screen, (0, 0, 0), background_rect)

    # Draw the welcome message on the screen
    screen.blit(welcome_text_line1, welcome_rect_line1)
    screen.blit(welcome_text_line2, welcome_rect_line2)

    # Load font for the welcome message
    #welcome_font = pygame.font.Font(None, 36)

    # Render the welcome message
    #welcome_text_line1 = welcome_font.render("Добро пожаловать на квиддич-чемпионат в Москве!", True, (255, 255, 255))
    #welcome_text_line2 = welcome_font.render("Приготовьте свою метлу, мы начинаем...", True, (255, 255, 255))

    # Get the rectangles for the welcome message texts
    #welcome_rect_line1 = welcome_text_line1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
    #welcome_rect_line2 = welcome_text_line2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))



    # Draw the welcome message on the screen
    #screen.blit(welcome_text_line1, welcome_rect_line1)
    #screen.blit(welcome_text_line2, welcome_rect_line2)

    # Update the display
    pygame.display.flip()

    # Wait for 5 seconds
    pygame.time.delay(10000)

hit_sound = pygame.mixer.Sound('sound/target catch.mp3')  # sound for hitting target

#Next level sounds
level_up_sound = pygame.mixer.Sound('sound/level up sound.mp3')
level_up_sound_1 = pygame.mixer.Sound('sound/level up sound 1.mp3')
level_up_sound_2 = pygame.mixer.Sound('sound/level up sound 2.mp3')
level_up_sound_3 = pygame.mixer.Sound('sound/level up sound 3.mp3')
level_sounds = [level_up_sound, level_up_sound_1, level_up_sound_2, level_up_sound_3]

#Main theme sound
main_theme_sound = pygame.mixer.Sound('sound/main theme.mp3')
main_theme_sound.play()


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

# Timer variables
start_time = pygame.time.get_ticks()  # Get the current time when the game starts
total_time = 10000  # Total time in milliseconds (10 seconds)




target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Variables for controlling the target's movement
target_speed = 1
target_direction_x = random.choice([-1, 1])
target_direction_y = random.choice([-1, 1])

# Define levels
levels = [
    {"duration": 20000},  # Level 1
    {"duration": 10000},  # Level 2
    {"duration": 10000},  # Level 3
    {"duration": 10000},  # Level 4
    {"duration": 15000},  # Level 5
    {"duration": 15000},  # Level 6
    {"duration": 15000},  # Level 7
    {"duration": 15000},  # Level 8
    {"duration": 15000},  # Level 9
    {"duration": 15000},  # Level 10
    {"duration": 15000},  # Level 11
    {"duration": 15000},  # Level 12
    {"duration": 15000},  # Level 13
    {"duration": 15000},  # Level 14
    {"duration": 15000},  # Level 15
    {"duration": 15000},  # Level 16
    {"duration": 15000},  # Level 17
    {"duration": 15000},  # Level 18
    {"duration": 15000},  # Level 19
    {"duration": 15000},  # Level 20
]

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def upper_line_1():#A1-A2
    y = (mouse_x - prev_target_x)*(target_y-prev_target_y)/(target_x - prev_target_x) + prev_target_y #y for the line at point mouse_x
    if mouse_y >= y:
        return True #means that the mouse is below the line and may belong to trajectory

def bottom_line_1 ():#B1 - B2
    y = (mouse_x - (prev_target_x+target_width)) * (target_y + target_width - (prev_target_y+target_height)) / (
                    target_x + target_width - (prev_target_x+target_width)) + prev_target_y+target_height  # y for the line at point mouse_x
    if mouse_y <= y:
        return True  # means that the mouse is above the line and may belong to trajectory
def upper_line_2():#C1 - C2
    y = (mouse_x - (prev_target_x+target_width))(target_y - prev_target_y)/(
            target_x+target_width - (prev_target_x + target_width)) + prev_target_y
    if mouse_y >= y:
        return True  # means that the mouse is above the line and may belong to trajectory
def bottom_line_2():#(D1-D2)
    y = ((mouse_x - prev_target_x)*(target_y + target_height - (prev_target_y+target_height))
         /(target_x-prev_target_x) + prev_target_y + target_height)
    if mouse_y <= y:
        return True  # means that the mouse is below the line and may belong to trajectory







    # Function to display popup message
def show_popup(message):
    #popup_font = pygame.font.Font(None, 24)
    #popup_surface = pygame.Surface((400, 200))
    #popup_surface.fill(WHITE)
    #popup_rect = popup_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    #popup_text = popup_font.render(message, True, WHITE)
    #text_rect = popup_text.get_rect(center=(popup_rect.width // 2, popup_rect.height // 2 - 20))
    #popup_surface.blit(popup_text, text_rect)

    # Load font for the popup message
    popup_font = pygame.font.Font(None, 24)

    # Render the text message
    popup_text = popup_font.render(message, True, WHITE)  # Render text with white color

    # Calculate the size of the popup rectangle based on the size of the text surface
    popup_rect = pygame.Rect((0, 0), (popup_text.get_width() + 40, popup_text.get_height() + 80))  # Add padding

    # Center the popup rectangle on the screen
    popup_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Draw the popup rectangle with a black outline
    pygame.draw.rect(screen, BLACK, popup_rect)

    # Draw the text message on the popup rectangle
    screen.blit(popup_text, popup_text.get_rect(center=popup_rect.center))

    button_exit = pygame.Rect(100, 500, 200, 50)
    button_retry = pygame.Rect(400, 500, 200, 50)
    button_font = pygame.font.Font(None, 45)
    exit_text = button_font.render("Выйти", True, WHITE)
    exit_rect = exit_text.get_rect(center=button_exit.center)
    retry_text = button_font.render("Повторить уровень", True, WHITE)
    retry_rect = retry_text.get_rect(center=button_retry.center)
    # Center button text on buttons
    retry_text_rect = retry_text.get_rect(center=button_retry.center)
    exit_text_rect = exit_text.get_rect(center=button_exit.center)

    # Draw buttons and text

    screen.blit(retry_text, retry_text_rect)
    screen.blit(exit_text, exit_text_rect)

    # Update the display
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_retry.collidepoint(mouse_pos):
                    pygame.mouse.set_visible(False)  # Hide the system cursor
                    cursor_rect = cursor_image.get_rect()
                    return "retry"  # Return "retry" if the retry button is pressed
                elif button_exit.collidepoint(mouse_pos):
                    pygame.mouse.set_visible(False)  # Hide the system cursor
                    cursor_rect = cursor_image.get_rect()
                    return "exit"  # Return "exit" if the exit button is pressed

        #screen.blit(popup_surface, popup_rect)


        #screen.blit(exit_text, exit_rect)
        #screen.blit(retry_text, retry_rect)
        pygame.mouse.set_visible(True)  # Показать курсор
        # Очистить предыдущее изображение курсора
        #screen.blit(background, pygame.mouse.get_pos(), pygame.Rect(pygame.mouse.get_pos(), cursor_rect.size))

        # Отобразить курсор
        #screen.blit(cursor_image, pygame.mouse.get_pos())
        pygame.display.flip()  # Обновить экран

# Load target GIF animation frames
target_animation_frames = []
for i in range(1, 45):  # because our animation has 45 frames
    frame = pygame.image.load(f"animation hit target/frame_{i}.gif").convert_alpha()
    frame = pygame.transform.scale(frame, (target_width, target_height))  # Adjust size as needed
    target_animation_frames.append(frame)


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

#creating previous coordinates for snitch
prev_target_x, prev_target_y = target_x, target_y


#Main loop

running = True
level = 0
clock = pygame.time.Clock()
welcome_displayed = False
points = 0
play_target_animation = False
animation_index = 0
animation_duration = 500  # Duration in milliseconds
animation_timer = 0

while running:
    #screen.fill(color)
    screen.blit(background, (0, 0))  # Draw the background image at coordinate (0,0)
    if not welcome_displayed:
        display_welcome_message()
        welcome_displayed = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 4< level < 9:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # trajectory_rect = pygame.Rect(min(prev_target_x, target_x), min(prev_target_y, target_y),
                #                               abs(target_x - prev_target_x) + target_width,
                #                               abs(target_y - prev_target_y) + target_height)
                # if trajectory_rect.collidepoint(mouse_x, mouse_y):
                #     points += 1
                #     hit_sound.play()
                #     play_target_animation = True
                #     animation_timer = pygame.time.get_ticks()
                if target_x > prev_target_x and target_y < prev_target_y:
                    trajectory_rect = pygame.Rect(prev_target_x, target_y,
                                                  target_x + target_width - prev_target_x,
                                                  prev_target_y+target_height-target_y)
                                                  #create a rectangle that encapsulates both positions
                    if trajectory_rect.collidepoint(mouse_x, mouse_y): #and upper_line_1() and bottom_line_1():
                        points += 1
                        hit_sound.play()
                        play_target_animation = True
                        animation_timer = pygame.time.get_ticks()

                elif target_x < prev_target_x and target_y > prev_target_y:
                    target_x, target_y, prev_target_x, prev_target_y = prev_target_x, prev_target_y,target_x, target_y
                    trajectory_rect = pygame.Rect(prev_target_x, target_y,
                                                  target_x + target_width - prev_target_x,
                                                  prev_target_y+target_height-target_y)
                                                  #create a rectangle that encapsulates both positions
                    if trajectory_rect.collidepoint(mouse_x, mouse_y):# and upper_line_1() and bottom_line_1():
                        points += 1
                        hit_sound.play()
                        play_target_animation = True
                        animation_timer = pygame.time.get_ticks()
                elif target_x > prev_target_x and target_y > prev_target_y:
                    trajectory_rect = pygame.Rect(prev_target_x, prev_target_y,
                                                  target_x + target_width - prev_target_x,
                                                  target_y + target_height - prev_target_y)
                    if trajectory_rect.collidepoint(mouse_x, mouse_y):# and upper_line_2() and bottom_line_2():
                        points += 1
                        hit_sound.play()
                        play_target_animation = True
                        animation_timer = pygame.time.get_ticks()

                elif target_x > prev_target_x and target_y > prev_target_y:
                    target_x, target_y, prev_target_x, prev_target_y = prev_target_x, prev_target_y, target_x, target_y
                    trajectory_rect = pygame.Rect(prev_target_x, prev_target_y,
                                                  target_x + target_width - prev_target_x,
                                                  target_y + target_height - prev_target_y)
                    if trajectory_rect.collidepoint(mouse_x, mouse_y): #and upper_line_2() and bottom_line_2():
                        points += 1
                        hit_sound.play()
                        play_target_animation = True
                        animation_timer = pygame.time.get_ticks()


            elif level >= 9:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                trajectory_rect = pygame.Rect(min(prev_target_x, target_x), min(prev_target_y, target_y),
                                               abs(target_x - prev_target_x) + target_width,
                                               abs(target_y - prev_target_y) + target_height)
                if trajectory_rect.collidepoint(mouse_x, mouse_y):
                     points += 1
                     hit_sound.play()
                     play_target_animation = True
                     animation_timer = pygame.time.get_ticks()




            else:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                    points += 1
                    hit_sound.play()
                    play_target_animation = True
                    animation_timer = pygame.time.get_ticks()

    # Draw timer
    #current_time = pygame.time.get_ticks()
    #time_left = max(total_time - (current_time - start_time), 0) // 1000  # Convert milliseconds to seconds
    #timer_text = font.render("Time: " + str(time_left), True, (255, 255, 255))
    #screen.blit(timer_text, (10, 50))

    # Draw timer
    current_time = pygame.time.get_ticks()
    time_left = max(levels[level]["duration"] - (current_time - start_time),
                    0) // 1000  # Convert milliseconds to seconds
    timer_text = font.render("Time left: " + str(time_left), True, (255, 255, 255))
    screen.blit(timer_text, (10, 50))

    # Get mouse position
    mouse_position = pygame.mouse.get_pos()

    # Set the position of the cursor image
    cursor_rect.center = mouse_position

    # Blit the cursor image at the mouse position
    screen.blit(cursor_image, cursor_rect)

    #save current coordinates as previous:
    prev_target_x, prev_target_y = target_x, target_y

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
     # Render points as text
    level_text = font.render("Level: " + str(level), True, (255, 255, 255))

    # Blit points text onto the screen at position (10, 10)
    screen.blit(level_text, (680, 10))
    #blits the target image onto the screen
    screen.blit(target_img, (target_x, target_y))

    # Draw target animation if triggered
    if play_target_animation:
        current_time = pygame.time.get_ticks()
        if current_time - animation_timer < animation_duration:
            screen.blit(target_animation_frames[animation_index], (target_x, target_y))
        else:
            play_target_animation = False
        animation_index = (animation_index + 1) % len(target_animation_frames)
    else:
        screen.blit(target_img, (target_x, target_y))  # Draw target image if animation is not playing

    if time_left == 0:
        action = show_popup("Время вышло. Потренируйтесь летать на метле и возвращайтесь!")
        if action == "retry":
            # Reset variables to repeat the level
            start_time = pygame.time.get_ticks()  # Reset the timer
            points = 0  # Reset points for the next level
            target_x = random.randint(0, SCREEN_WIDTH - target_width)  # Reset target position
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        elif action == "exit":
            pygame.quit()
            sys.exit()


    # go up a level increasing speed
    if points >= 5:
        random_level_up_sound = random.choice(level_sounds)
        random_level_up_sound.play()
        level += 1  # Move to the next level
        if level < len(levels):
            target_speed += 1  # Increase target speed for next level
            background= random.choice(background_images)
            screen.blit(background, (0, 0))  # Draw the new background
            pygame.display.flip()
            pygame.time.wait(500)  # Wait for 2 seconds before starting the next level
            start_time = pygame.time.get_ticks()  # Reset the timer
            points = 0  # Reset points for the next level
            target_x = random.randint(0, SCREEN_WIDTH - target_width)  # Reset target position
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        else:
            running = False  # End the game if all levels are completed

    #pygame.display.update()
    # Update the display
    pygame.display.flip()

    clock.tick(60)  # Limit frame rate to 60 FPS


pygame.quit()
sys.exit()