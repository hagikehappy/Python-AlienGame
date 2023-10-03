import sys

import pygame

from settings import Settings


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings().config

        self.screen = pygame.display.set_mode((self.settings['screen_width'], self.settings['screen_height']))
        pygame.display.set_caption(self.settings['caption'])

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 画图
            self.screen.fill(self.settings['bg_color'])

            # 刷新显示
            pygame.display.flip()
            self.clock.tick(self.settings['refresh_rate'])


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
