import pygame
from time import sleep


class Collision:
    """用于处理与碰撞相关的系列操作"""

    def __init__(self, ai_game):
        """初始化碰撞"""
        self.ai_game = ai_game

    def collide_check(self):
        """检测是否发生碰撞"""
        # 检测子弹和外星人
        pygame.sprite.groupcollide(self.ai_game.all_bullets.bullets, self.ai_game.all_aliens.aliens, True, True)
        # 检测飞船和外星人
        if pygame.sprite.spritecollideany(self.ai_game.ship, self.ai_game.all_aliens.aliens):
            self._ship_hit()
        # 检测外星人和底边
        self._check_aliens_bottom()

    def _ship_hit(self):
        """处理船与子弹碰撞情况"""
        # 记录飞船损失
        self.ai_game.game_stats.ships_left -= 1
        # 清空外星人列表和子弹列表
        self.ai_game.all_bullets.bullets.empty()
        self.ai_game.all_aliens.aliens.empty()
        # 创建一个新的外星舰队i并初始化飞船
        self.ai_game.all_aliens.create_fleet()
        self.ai_game.ship.center_ship()
        # 刷新屏幕
        self.ai_game.game_stats.game_check()
        if self.ai_game.game_stats.ships_left > 0:
            self.ai_game.update_screen()
            # 缓冲一段时间
            sleep(2)

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕的下边缘"""
        for alien in self.ai_game.all_aliens.aliens:
            if alien.rect.bottom >= self.ai_game.screen_rect.height:
                # 像被飞船撞到那样处理
                self._ship_hit()
                break
