import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船所发射的子弹类"""

    def __init__(self, ai_game):
        """在飞船的当前位置创建一个子弹类"""
        super().__init__()
        self.screen = ai_game.screen
        self.color = ai_game.settings['bullet_color']
        self.speed = ai_game.settings['bullet_speed']
        self.rect = pygame.Rect(0, 0, ai_game.settings['bullet_width'], ai_game.settings['bullet_height'])
        self.rect.midtop = ai_game.ship.rect.midtop
        self.one_y = ai_game.settings['one_y'] * self.speed * 240 / ai_game.settings['refresh_rate']

    def update(self):
        """更新子弹位置"""
        self.rect.y -= self.one_y

    def draw_bullet(self):
        """画出子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
