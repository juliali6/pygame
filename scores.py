import pygame.font
from gun import Gun
from pygame.sprite import Group


class Scores():
    """Вывод игровой информации"""

    def __init__(self, screen, stats):
        """Инициализация подсчета очков"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 242, 0 )
        self.font = pygame.font.SysFont(None, 36)  # шрифт по умолчанию нон и размер 36
        self.image_score()  # текущий счет
        self.image_high_score()  # рекорд
        self.image_guns()  # вывод к-л жизней

    def image_score(self):
        """Преобразовывает текст счета в графическое изображение"""

        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40  # размещение счета в углу правой части экрана
        self.score_rect.top = 20

    def image_high_score(self):
        """Преобразовывает рекорд в графическое изображение"""

        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_guns(self):
        """К-л жизней"""

        self.guns = Group()
        for gun_number in range(self.stats.gun_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        """Вывод счета на экран"""

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)






