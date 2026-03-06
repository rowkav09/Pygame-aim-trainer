import sys

import pygame
from pygame.locals import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((1080, 1080), HWSURFACE | DOUBLEBUF | RESIZABLE)
    fake_screen = screen.copy()
    font = pygame.font.SysFont(name="mechanical", size=48)
    pic = pygame.surface.Surface((50, 500))
    text = font.render("Aim train", True, (255, 255, 0))
    screen.blit(text, dest=(300, 100))
    pic.fill((255, 100, 200))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

        screen.fill((0, 0, 0))
        fake_screen.fill('black')
        fake_screen.blit(pic, (100, 100))
        fake_screen.blit(text, (100, 100))
        screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))


        #pygame.draw.rect(surface=screen, color=(0, 255, 255), rect=(100, 100, 200, 200))
        #pygame.draw.circle(surface=screen, color=(255, 0, 255), center=(300, 150), radius=100)


        #text_surface = font.render("Hello World", True, (255, 255, 0))
        #screen.blit(text_surface, dest=(300, 100))

        pygame.display.flip()

main()
