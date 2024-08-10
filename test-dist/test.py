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
text = font.render("TestOS", True, black)
text_rect = text.get_rect(center=(screen_width//2, screen_height//2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill(white)

    screen.blit(text, text_rect)

    pygame.display.flip()
