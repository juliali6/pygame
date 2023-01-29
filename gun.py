import pygame


class Gun():

    def __init__(self, screen):
        """Инициализация пушки"""

        self.screen = screen
        self.image = pygame.image.load('image/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx  # координаты центра пушки
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        """Рисование пушки"""

        self.screen.blit(self.image, self.rect)
