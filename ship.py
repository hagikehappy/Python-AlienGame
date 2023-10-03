import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.ship_speed = ai_game.settings['ship_speed']
        self.one_x = ai_game.settings['one_x'] * self.ship_speed * 240 / ai_game.settings['refresh_rate']
        self.one_y = ai_game.settings['one_y'] * self.ship_speed * 240 / ai_game.settings['refresh_rate']

        # 加载飞船图像并获取外接矩阵
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 每艘性飞船都放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right:
            self.rect.x += self.one_x
        if self.moving_left:
            self.rect.x -= self.one_x

    def blitme(self):
        """在指定位置创建飞船"""
        self.screen.blit(self.image, self.rect)
