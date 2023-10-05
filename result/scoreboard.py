import  pygame.font


class Scoreboard:
    """显示得分信息的类"""

    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.ai_game = ai_game
        # 显示得分信息时所用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 96)
        # 准备初始得分图像
        self.score_image = None
        self.score_rect = None
        self.prep_score()

    def prep_score(self):
        """将得分渲染为图像"""
        score_str = str(self.ai_game.game_stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.ai_game.bg_color)
        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.ai_game.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.ai_game.screen.blit(self.score_image, self.score_rect)
