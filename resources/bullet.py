import pygame
from pygame.sprite import Sprite
import copy


class Bullet(Sprite):
    """飞船所发射的一颗子弹"""

    def __init__(self, all_bullets, init_info):
        """在飞船的当前位置创建一个子弹类"""
        super().__init__()
        self.all_bullets = all_bullets
        self.rect = copy.deepcopy(all_bullets.rect)
        self.rect.midtop = init_info[0]
        self.one_y = all_bullets.one_y

    def update(self):
        """更新子弹位置"""
        self.rect.y -= self.one_y

    def draw_bullet(self):
        """画出子弹"""
        pygame.draw.rect(self.all_bullets.screen, self.all_bullets.color, self.rect)


class All_Bullets:
    """管理飞船所发射的所有子弹"""

    def __init__(self, ai_game):
        """初始化子弹类"""
        self.ai_game = ai_game
        self.bullets = pygame.sprite.Group()
        self.bullets_num = 0
        self.base_interval = 1.0 / ai_game.refresh_rate
        self.next_interval = ai_game.settings['bullet_interval']
        self.bullets_interval = 0.0
        self.fire_interval = False
        # 通用子弹设置
        self._common_settings()

    def reinitialize_bullets(self):
        """重置子弹类"""
        pass

    def _common_settings(self):
        """所有子弹的通用设置"""
        self.screen = self.ai_game.screen
        self.color = self.ai_game.settings['bullet_color']
        self.speed = self.ai_game.settings['bullet_speed']
        self.rect = pygame.Rect(0, 0, self.ai_game.settings['bullet_width'], self.ai_game.settings['bullet_height'])
        self.one_y = self.ai_game.settings['one_y'] * self.speed * 240 / self.ai_game.refresh_rate

    def _fire_bullet(self):
        """开火后根据条件创建一颗新子弹"""
        if (self.bullets_interval == 0.0) or (self.bullets_interval > self.next_interval):
            if self.bullets_interval != 0.0:
                self.bullets_interval -= self.next_interval
            if self.bullets_num < self.ai_game.settings['bullet_max']:
                self.bullets.add(Bullet(self,
                                        (self.ai_game.ship.rect.midtop, )))
        self.bullets_interval += self.base_interval

    def _clear_bullet(self):
        """清除飞出的子弹"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def update(self):
        """更新子弹状态"""
        self._clear_bullet()
        self.bullets_num = len(self.bullets)
        if self.fire_interval is True:
            self._fire_bullet()
        self.bullets.update()

    def draw_bullets(self):
        """画出所有的子弹"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
