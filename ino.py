import pygame


class Ino(pygame.sprite.Sprite):
    """Класс одного пришельца"""

    def __init__(self, screen):
        """Инициализируем и задаем начальную позицию"""

        super(Ino, self).__init__()
        self.screen = screen  # отрисовываем экран, где происходит действие самой игры
        self.image = pygame.image.load('image/ine.png')  # загружаем изображение
        self.rect = self.image.get_rect()  # помещаем изображение в верхнюю часть экрана
        self.rect.x = self.rect.width  # помещаем изображение в левый угол, отслеживаем ширину
        self.rect.y = self.rect.height  # отслеживаем высоту

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Вывод пришельца на экран"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещение пришельцев"""

        self.y += 0.1
        self.rect.y = self.y

