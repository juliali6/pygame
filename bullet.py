import pygame


class Bullet(pygame.sprite.Sprite):  # дочерний класс

    def __init__(self, screen, gun):
        """Создаем пулю в позиции пушки"""

        super(Bullet, self).__init__()   # метод super для дочернего класса
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 30, 12)  # размер пули
        self.color = 255, 242, 0  # цвет пули
        self.speed = 4.5  # скорость пути
        self.rect.centerx = gun.rect.centerx  # координаты пули
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пути вверх"""

        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисуем пулю на экране"""

        pygame.draw.rect(self.screen, self.color, self.rect)


