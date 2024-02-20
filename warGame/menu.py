import pygame
import sys
import main  # Import the main module containing the game loop

# Initialize Pygame
pygame.init()

# Set up screen dimensions
WIDTH, HEIGHT = 750, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter - Main Menu")

# Load background image
BACKGROUND_IMAGE = pygame.image.load("background_image.jpg")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

# Button colors
BUTTON_COLOR = (0, 255, 0)
HOVER_COLOR = (0, 200, 0)

# Fonts
FONT = pygame.font.Font(None, 40)

# Function to draw text on screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    SCREEN.blit(text_surface, text_rect)

# Function to draw buttons
def draw_button(x, y, width, height, color, hover_color, text, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(SCREEN, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            if action == "start":
                main.main()  # Call the main function from the main module
            elif action == "settings":
                # Add code to open settings menu
                pass
            elif action == "high_scores":
                # Add code to view high scores
                pass
            elif action == "exit":
                pygame.quit()
                sys.exit()
    else:
        pygame.draw.rect(SCREEN, color, (x, y, width, height))

    draw_text(text, FONT, (255, 255, 255), x + width / 2, y + height / 2)

# Main menu loop
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw background image
        SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

        # Draw menu buttons
        draw_button(250, 250, 250, 50, BUTTON_COLOR, HOVER_COLOR, "Start Game", action="start")
        draw_button(250, 320, 250, 50, BUTTON_COLOR, HOVER_COLOR, "Settings", action="settings")
        draw_button(250, 390, 250, 50, BUTTON_COLOR, HOVER_COLOR, "High Scores", action="high_scores")
        draw_button(250, 460, 250, 50, BUTTON_COLOR, HOVER_COLOR, "Exit", action="exit")

        pygame.display.update()

if __name__ == "__main__":
    main_menu()

