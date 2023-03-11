class Stats():
    """Отслеживание статистики"""

    def __init__(self):
        """Инициализация статистики"""

        self.reset_stats()
        self.run_game = True
        with open('hightscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """Изменяющаяся статистика во время игры"""

        self.gun_left = 2  # к-л жизней
        self.score = 0  # счет
