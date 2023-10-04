import pygame
from pygame.sprite import Sprite
import random
from config.extern_var import *


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, all_aliens, init_info=None):
        """初始化外星人并设置其初始位置"""
        super().__init__()
        self.all_aliens = all_aliens
        self.image = all_aliens.image
        self.rect = all_aliens.image.get_rect()
        self.one_x = all_aliens.one_x
        self.one_y = all_aliens.one_y

        # 使每个外星人最初都在指定位置
        # 如果没有指定则在屏幕的左上角离边缘有一个外星人间隔的距离
        if init_info is None:
            self.rect.centerx = self.rect.width
            self.rect.centery = self.rect.height
        else:
            self.rect.centerx = init_info[0]
            self.rect.centery = init_info[1]

    def _update_speed(self):
        """个性化的更新速度"""
        self.one_x = self.all_aliens.one_x
        self.one_y = self.all_aliens.one_y

    def check_edges(self):
        """边缘检测"""
        return (self.rect.right >= self.all_aliens.screen_rect.right) or \
            (self.rect.left <= self.all_aliens.screen_rect.left)

    def update(self, fleet_direction_lr, fleet_direction_down):
        """对于单个外星人的更新方法"""
        self._update_speed()
        self.rect.x += fleet_direction_lr * self.one_x
        if fleet_direction_down:
            self.rect.y += self.one_y


class All_Aliens:
    """对于全体外星人的控制方法"""

    def __init__(self, ai_game):
        """创建外星人编组"""
        self.ai_game = ai_game
        self.aliens = pygame.sprite.Group()
        self.alien_init_row = ai_game.settings['alien_init_row']
        self.alien_init_col = ai_game.settings['alien_init_col']
        self.alien_init_num = self.alien_init_col * self.alien_init_row
        self.alien_num = self.alien_init_num
        self.rate_per_alien = 1 / self.alien_init_num
        self.alien_init_cover_rate = ai_game.settings['alien_init_cover_rate']
        self.alien_width = ai_game.screen_rect.width / (self.alien_init_col + 1)
        self.alien_height = ai_game.screen_rect.height * self.alien_init_cover_rate / (self.alien_init_row + 1)
        self.fleet_direction_lr = LEFT_FORWARD
        self.fleet_direction_down = False
        # 公用外星人初始化配置
        self._common_settings()
        # 创建初始舰队
        self._create_fleet()

    def _common_settings(self):
        """所有外星人共享的通用设置"""
        self.screen = self.ai_game.screen
        self.screen_rect = self.ai_game.screen_rect
        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        # 初始化外星人属性
        self.lr_speed = self.ai_game.settings['alien_init_lr_speed']
        self.down_speed = self.ai_game.settings['alien_init_down_speed']
        self.one_x = self.ai_game.settings['one_x'] * self.lr_speed * 240 / self.ai_game.settings['refresh_rate']
        self.one_y = self.ai_game.settings['one_y'] * self.down_speed * 240 / self.ai_game.settings['refresh_rate']
        self.one_init_x = self.one_x
        self.one_init_y = self.one_y
        # 速度变换类属性初始化与标准化过程
        # 随时间，标准化至单帧
        self.x_speed_time_up = self.ai_game.settings['alien_lr_speed_time_up'] / self.ai_game.refresh_rate
        self.x_speed_time_already_up = 1
        self.x_speed_time_max = self.ai_game.settings['alien_lr_speed_time_max']
        self.y_speed_time_up = self.ai_game.settings['alien_down_speed_time_up'] / self.ai_game.refresh_rate
        self.y_speed_time_already_up = 1
        self.y_speed_time_max = self.ai_game.settings['alien_down_speed_time_max']
        # 随敌人数量
        self.x_speed_num_up = self.ai_game.settings['alien_lr_speed_num_up']
        self.x_speed_num_already_up = 1
        self.x_speed_num_max = self.ai_game.settings['alien_lr_speed_num_max']
        self.y_speed_num_up = self.ai_game.settings['alien_down_speed_num_up']
        self.y_speed_num_already_up = 1
        self.y_speed_num_max = self.ai_game.settings['alien_down_speed_num_max']

    def _create_alien(self, init_info=None):
        """创建一个外星人"""
        self.aliens.add(Alien(self, init_info))

    def _new_alien(self):
        """创建新的一排外星人"""
        new_flag = True
        for alien in self.aliens:
            if alien.rect.centery < self.alien_width:
                new_flag = False
                break
        if new_flag:
            for i in range(1, self.alien_init_col + 1):
                self._create_alien(((i + random.uniform(-0.3, 0.3)) * self.alien_width,
                                    (1 + random.uniform(-0.3, 0.3)) * self.alien_height))

    def _update_speed(self):
        """通用的更新外星人速度"""
        # x方向更新
        if self.x_speed_time_already_up < self.x_speed_time_max:
            self.x_speed_time_already_up += self.x_speed_time_up
        self.x_speed_num_already_up = 1 + (self.alien_init_num - self.alien_num) * self.x_speed_num_up
        if self.x_speed_num_already_up > self.x_speed_num_max:
            self.x_speed_num_already_up = self.x_speed_num_max
        if self.x_speed_num_already_up < self.lr_speed:
            self.x_speed_num_already_up = 1
        # y方向更新
        if self.y_speed_time_already_up < self.y_speed_time_max:
            self.y_speed_time_already_up += self.y_speed_time_up
        self.y_speed_num_already_up = 1 + (self.alien_init_num - self.alien_num) * self.y_speed_num_up
        if self.y_speed_num_already_up > self.y_speed_num_max:
            self.y_speed_num_already_up = self.y_speed_num_max
        if self.y_speed_num_already_up < self.down_speed:
            self.y_speed_num_already_up = 1
        # 综合更新
        self.one_x = self.one_init_x * self.x_speed_time_already_up * self.x_speed_num_already_up
        self.one_y = self.one_init_y * self.y_speed_time_already_up * self.y_speed_num_already_up

    def _create_fleet(self):
        """创建一个外星舰队"""
        # 创建一阵列外星人
        for i in range(1, self.alien_init_col + 1):
            for j in range(1, self.alien_init_row + 1):
                self._create_alien(((i + random.uniform(-0.3, 0.3)) * self.alien_width,
                                    (j + random.uniform(-0.3, 0.3)) * self.alien_height))

    def _check_all_edges(self):
        """检测全体外星人边缘"""
        for alien in self.aliens:
            if alien.check_edges():
                self.fleet_direction_lr = -self.fleet_direction_lr
                self.fleet_direction_down = True
                break

    def update(self):
        """更新全体外星人状态"""
        self._new_alien()
        self._check_all_edges()
        self.alien_num = len(self.aliens)
        self._update_speed()
        self.aliens.update(self.fleet_direction_lr, self.fleet_direction_down)
        self.fleet_direction_down = False
