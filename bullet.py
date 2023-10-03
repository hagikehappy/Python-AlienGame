import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """飞船所发射的一颗子弹"""

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


class All_Bullets:
    """管理飞船所发射的所有子弹"""

    def __init__(self, ai_game):
        """初始化子弹类"""
        self.ai_game = ai_game
        self.bullets = pygame.sprite.Group()
        self.bullets_num = 0

    def fire_bullet(self):
        """开火后创建一颗新子弹"""
        if self.bullets_num < self.ai_game.settings['bullet_max']:
            self.bullets.add(Bullet(self.ai_game))
            self.bullets_num += 1

    def _clear_bullet(self):
        """清除飞出的子弹"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                self.bullets_num -= 1

    def update(self):
        """更新子弹状态"""
        self._clear_bullet()
        self.bullets.update()

    def draw_bullets(self):
        """画出所有的子弹"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
