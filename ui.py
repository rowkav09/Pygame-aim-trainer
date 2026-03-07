import sys
import pygame
from pygame.locals import *

TRAINER_TYPES = ["Static Targets", "Tracking", "Flicking"]
RESOLUTIONS   = [(1920, 1080), (1280, 960), (1024, 768), (1280, 1024)]
RES_LABELS    = ["1920x1080", "1280x960", "1024x768", "1280x1024"]

BG      = (15, 15, 20)
PANEL   = (30, 30, 40)
ACCENT  = (255, 200, 0)
WHITE   = (220, 220, 220)
GREY    = (100, 100, 110)
BTN     = (45, 45, 60)
BTN_HOV = (65, 65, 85)


def centered_text(surf, text, font, colour, cx, y):
    img = font.render(text, True, colour)
    surf.blit(img, (cx - img.get_width() // 2, y))


def arrow_selector(surf, font, label, value, x, y, w, h, mx, my):
    lbl = font.render(label, True, GREY)
    surf.blit(lbl, (x, y - 26))

    pygame.draw.rect(surf, PANEL, (x, y, w, h), border_radius=6)
    pygame.draw.rect(surf, ACCENT, (x, y, w, h), 1, border_radius=6)

    aw = 36
    left_rect  = pygame.Rect(x, y, aw, h)
    right_rect = pygame.Rect(x + w - aw, y, aw, h)

    pygame.draw.rect(surf, BTN_HOV if left_rect.collidepoint(mx, my)  else BTN, left_rect,  border_radius=6)
    pygame.draw.rect(surf, BTN_HOV if right_rect.collidepoint(mx, my) else BTN, right_rect, border_radius=6)

    la = font.render("<", True, ACCENT)
    ra = font.render(">", True, ACCENT)
    surf.blit(la, la.get_rect(center=left_rect.center))
    surf.blit(ra, ra.get_rect(center=right_rect.center))

    val = font.render(value, True, WHITE)
    surf.blit(val, val.get_rect(center=(x + w // 2, y + h // 2)))

    return left_rect, right_rect


def menu():
    W, H = 720, 500
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Aim Trainer")
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("arial", 50, bold=True)
    font       = pygame.font.SysFont("arial", 24)
    small_font = pygame.font.SysFont("arial", 18)

    sel_trainer = 0
    sel_res     = 0
    sens        = 1.0

    BOX_W = 280
    BOX_H = 44
    COL_L = 60
    COL_R = W - 60 - BOX_W

    Y_TRAINER = 170
    Y_RES     = 290
    Y_SENS    = 170

    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        start_rect = pygame.Rect(W // 2 - 105, H - 90, 210, 50)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                tl = pygame.Rect(COL_L, Y_TRAINER, 36, BOX_H)
                tr = pygame.Rect(COL_L + BOX_W - 36, Y_TRAINER, 36, BOX_H)
                rl = pygame.Rect(COL_L, Y_RES, 36, BOX_H)
                rr = pygame.Rect(COL_L + BOX_W - 36, Y_RES, 36, BOX_H)
                sl = pygame.Rect(COL_R, Y_SENS, 36, BOX_H)
                sr = pygame.Rect(COL_R + BOX_W - 36, Y_SENS, 36, BOX_H)

                if tl.collidepoint(mx, my):
                    sel_trainer = (sel_trainer - 1) % len(TRAINER_TYPES)
                elif tr.collidepoint(mx, my):
                    sel_trainer = (sel_trainer + 1) % len(TRAINER_TYPES)
                elif rl.collidepoint(mx, my):
                    sel_res = (sel_res - 1) % len(RESOLUTIONS)
                elif rr.collidepoint(mx, my):
                    sel_res = (sel_res + 1) % len(RESOLUTIONS)
                elif sl.collidepoint(mx, my):
                    sens = round(max(0.1, sens - 0.1), 1)
                elif sr.collidepoint(mx, my):
                    sens = round(min(10.0, sens + 0.1), 1)
                elif start_rect.collidepoint(mx, my):
                    running = False

        screen.fill(BG)

        centered_text(screen, "AIM TRAINER", title_font, ACCENT, W // 2, 28)
        pygame.draw.line(screen, GREY, (50, 100), (W - 50, 100), 1)
        centered_text(screen, "Configure your session", small_font, GREY, W // 2, 110)

        arrow_selector(screen, font, "TRAINER TYPE", TRAINER_TYPES[sel_trainer],
                       COL_L, Y_TRAINER, BOX_W, BOX_H, mx, my)
        arrow_selector(screen, font, "RESOLUTION", RES_LABELS[sel_res],
                       COL_L, Y_RES, BOX_W, BOX_H, mx, my)
        arrow_selector(screen, font, "SENSITIVITY", f"{sens:.1f}",
                       COL_R, Y_SENS, BOX_W, BOX_H, mx, my)

        btn_col = BTN_HOV if start_rect.collidepoint(mx, my) else BTN
        pygame.draw.rect(screen, btn_col, start_rect, border_radius=8)
        pygame.draw.rect(screen, ACCENT, start_rect, 2, border_radius=8)
        centered_text(screen, "START", font, ACCENT,
                      start_rect.centerx, start_rect.centery - font.get_height() // 2)

        centered_text(screen, "ESC to quit", small_font, GREY, W // 2, H - 20)

        pygame.display.flip()
        clock.tick(60)

    return {
        "trainer_type": TRAINER_TYPES[sel_trainer],
        "resolution":   RESOLUTIONS[sel_res],
        "sens":         sens,
    }
