import sys
import pygame
from pygame.locals import *


def run_aim_trainer(settings):
    res = settings["resolution"]
    screen = pygame.display.set_mode(res, HWSURFACE | DOUBLEBUF | RESIZABLE)
    pygame.display.set_caption(f"Aim Trainer – {settings['trainer_type']}")
    fake_screen = pygame.Surface(res)
    font  = pygame.font.SysFont("arial", 30)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)

        fake_screen.fill((15, 15, 20))

        # ── your aim trainer code goes here ──────────────────────────────────
        info = font.render(
            f"{settings['trainer_type']}  |  {res[0]}x{res[1]}  |  sens {settings['sens']}",
            True, (255, 200, 0)
        )
        fake_screen.blit(info, (20, 20))

        # stretch res: scale fake_screen to whatever the window size is
        screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
        pygame.display.flip()
        clock.tick(60)
