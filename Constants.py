import pygame
import math

# Initialize Pygame
pygame.init()

# Screen Size
WIDTH, HEIGHT = 800, 600

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (64,64,64)
GREEN = (0,64,0)
RED = (64,0,0)

# Define some font sizes
font_name = "MSGothic"
large_font = pygame.font.SysFont(font_name, 80)
question_font = pygame.font.SysFont(font_name, 50)
medium_font = pygame.font.SysFont(font_name, 30)
small_font = pygame.font.SysFont(font_name, 20)

# Define screen dimensions
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the score variables
answer_spacing = math.floor((medium_font.get_height()*1.34))