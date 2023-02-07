import pygame, sys
from bullet import Bullet
from ino import Ino


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


def update(bg_color, screen, gun, inos, bullets):
    """Обновление экрана"""

    screen.fill(bg_color)  # фоновый цвет
    for bullet in bullets.sprites():  # метод sprites вернет все элементы
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)  # отрисовываем пришельцев на экране
    pygame.display.flip()


def update_bullets(bullets):
    """Обновление позиции пуль"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # print(len(bullets))  # вывод к-л пулек на экране


def update_inos(inos):
    """Обновляет позицию пришельцев"""

    inos.update()


def create_army(screen, inos):
    """Создание армии пришельцев"""

    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)  # один ряд пришельцев
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)





