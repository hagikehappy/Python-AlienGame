import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings().config

        # 屏幕设置
        if not self.settings['fullscreen']:
            self.screen = pygame.display.set_mode((self.settings['screen_width'], self.settings['screen_height']))
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.screen_rect = self.screen.get_rect()
        if self.settings['fullscreen']:
            self.settings['screen_width'] = self.screen_rect.width
            self.settings['one_x'] = self.settings['screen_width'] / 1000
            self.settings['screen_height'] = self.screen_rect.height
            self.settings['one_y'] = self.settings['screen_height'] / 1000

        pygame.display.set_caption(self.settings['caption'])

        # 游戏资源初始化
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bullet_num = 0

    def _check_keydown_events(self, event):
        """按下按键时发生的事情"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """抬起按键时发生的事情"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _fire_bullet(self):
        """开火后创建一颗新子弹"""
        if self.bullet_num < self.settings['bullet_max']:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.bullet_num += 1

    def _clear_bullet(self):
        """清除飞出的子弹"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                self.bullet_num -= 1

    def _update_things(self):
        """更新场上资源"""
        self.ship.update()
        self._clear_bullet()
        self.bullets.update()

    def _update_screen(self):
        """画图"""
        self.screen.fill(self.settings['bg_color'])
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 刷新显示
        pygame.display.flip()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_things()
            self._update_screen()
            self.clock.tick(self.settings['refresh_rate'])


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
