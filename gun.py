import pygame


class Gun():

    def __init__(self, screen):
        """Инициализация пушки"""

        self.screen = screen
        self.image = pygame.image.load('image/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx  # координаты центра пушки
        self.center = float(self.rect.centerx)  # движение пушки
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False  # движение пушки вправо
        self.mleft = False  # движение пушки влево

    def output(self):
        """Рисование пушки"""

        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """Обновление позиции пушки"""

        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1  # интервал движения пушки вправо
        if self.mleft and self.rect.left > 0:
            self.center -= 1  # интервал движения пушки влево

        self.rect.centerx = self.center

