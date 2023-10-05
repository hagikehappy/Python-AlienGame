

class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.ai_game = ai_game
        self._reset_stats()

    def _reset_stats(self):
        """初始化在游戏运行中可能变化的统计信息"""
        self.ships_init = self.ai_game.settings['ship_limits']
        self.ships_left = self.ships_init
        self.game_active = True

    def game_check(self):
        """检测游戏活动状态"""
        if self.ships_left <= 0:
            self.game_active = False
