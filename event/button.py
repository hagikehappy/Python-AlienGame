import pygame.font
from pygame.sprite import Sprite
from event.button_event import *


class Button(Sprite):
    """为游戏创建单个按钮管理"""

    def __init__(self, all_buttons, msg, rect_center, event=None):
        """初始化按钮的自有属性"""
        super().__init__()
        self.all_buttons = all_buttons
        self.msg = msg
        self.event = event
        self.button_rect = pygame.Rect(0, 0, self.all_buttons.button_width, self.all_buttons.button_height)
        self.button_rect.center = rect_center
        self.button_color = list(self.all_buttons.button_color)
        self.mouse_event = all_buttons.button_event.event_dict[event]
        self.msg_image = None
        self.msg_image_rect = None
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.all_buttons.font.render(msg, True,
                                                      self.all_buttons.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.button_rect.center

    def draw_button(self):
        """实际绘制单个按钮"""
        self.all_buttons.ai_game.screen.fill(self.button_color, self.button_rect)
        self.all_buttons.ai_game.screen.blit(self.msg_image, self.msg_image_rect)


class All_Buttons:
    """为游戏创建按钮的总体管理"""

    def __init__(self, ai_game):
        """初始化按钮的通用属性"""
        self.ai_game = ai_game
        self.buttons = pygame.sprite.Group()
        self._common_settings()
        # 实例化Event列表
        self.button_event = Button_Event(ai_game, self)
        # 创建起始按钮
        self._create_button('Play', self.ai_game.screen_rect.center, Event_Dict.AT_BEGIN)

    def _common_settings(self):
        """通用初始化属性"""
        self.button_width = self.ai_game.screen_rect.width / 10
        self.button_height = self.ai_game.screen_rect.height / 10
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 96)

    def _create_button(self, msg, rect_center, event):
        """创建按钮"""
        self.buttons.add(Button(self, msg, rect_center, event))

    def clear_button(self, button):
        """删除指定按钮"""
        self.buttons.remove(button)

    def clear_all_button(self):
        """清空全部按钮"""
        self.buttons.empty()

    def draw_buttons(self):
        """绘制全体按钮"""
        for button in self.buttons.sprites():
            button.draw_button()
