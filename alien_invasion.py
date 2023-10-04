import sys

import pygame

from config.settings import Settings
from resources.ship import Ship
from resources.bullet import All_Bullets
from resources.alien import All_Aliens


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings().config
        self.bg_color = self.settings['bg_color']
        self.refresh_rate = self.settings['refresh_rate']

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
        self.all_bullets = All_Bullets(self)
        self.all_aliens = All_Aliens(self)

    def _check_keydown_events(self, event):
        """按下按键时发生的事情"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self.all_bullets.fire_interval = True
            self.all_bullets.bullets_interval = 0.0
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """抬起按键时发生的事情"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_SPACE:
            self.all_bullets.fire_interval = False

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_things(self):
        """更新场上资源"""
        self.ship.update()
        self.all_bullets.update()
        self.all_aliens.update()
        # 碰撞检测，清除外星人
        pygame.sprite.groupcollide(self.all_bullets.bullets, self.all_aliens.aliens, True, True)

    def _update_screen(self):
        """画图"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.all_bullets.draw_bullets()
        # 此处直接调用sprite中的draw而无需自己创建draw方法
        self.all_aliens.aliens.draw(self.screen)

        # 刷新显示
        pygame.display.flip()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_things()
            self._update_screen()
            self.clock.tick(self.refresh_rate)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
