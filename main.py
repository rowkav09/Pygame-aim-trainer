import pygame
from ui import menu
from aim_trainer import run_aim_trainer

def main():
    pygame.init()
    settings = menu()
    run_aim_trainer(settings)

main()
