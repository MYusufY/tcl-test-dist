import pygame
import sys

pygame.init()

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.Font(None, 150)
text = font.render("TEST", True, black)
text_rect = text.get_rect(center=(screen_width//2, screen_height//2))

while True:
    screen.fill(white)

    screen.blit(text, text_rect)

    pygame.display.flip()
