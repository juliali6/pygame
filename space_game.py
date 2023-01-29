import pygame
import sys
from gun import Gun


def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))  # размер экрана
    pygame.display.set_caption("Космические защитники")  # заголовок
    bg_color = (0, 0, 0)  # цвет черный
    gun = Gun(screen)  # объект пушки

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)  # фоновый цвет
        gun.output()
        pygame.display.flip()


run()

