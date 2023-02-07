import pygame, controls
from gun import Gun
from pygame.sprite import Group


def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))  # размер экрана
    pygame.display.set_caption("Космические защитники")  # заголовок
    bg_color = (0, 0, 0)  # цвет черный
    gun = Gun(screen)  # объект пушки
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullets(bullets)
        controls.update_inos(inos)


run()



