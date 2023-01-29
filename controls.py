import pygame, sys
from bullet import Bullet


def events(screen, gun, bullets):
    """Обработка событие. Нажатие на какую-либо клавишу."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # кнопка вправо
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:  # кнопка влево
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:  # кнопка вправо
            if event.key == pygame. K_d:
                gun.mright = False
            elif event.key == pygame.K_a:  # кнопка влево
                gun.mleft = False


def update(bg_color, screen, gun, bullets):
    """Обновление экрана"""

    screen.fill(bg_color)  # фоновый цвет
    for bullet in bullets.sprites():  # метод sprites вернет все элементы
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()


def update_bullets(bullets):
    """Обновление позиции пуль"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # print(len(bullets))  # вывод к-л пулек на экране









