from enum import Enum
import pygame


class Event_Dict(Enum):
    """此处定义了所有的按键事件"""
    AT_BEGIN = 1



class Button_Event:
    """按键事件定义"""

    def __init__(self, ai_game, all_buttons):
        """初始化事件表"""
        self.ai_game = ai_game
        self.all_buttons = all_buttons
        self.event_dict = {}
        self.event_dict[Event_Dict.AT_BEGIN] = self.at_begin_event

    def at_begin_event(self, mouse, button):
        """初始页面抬起按钮行为"""
        if mouse == pygame.MOUSEBUTTONUP:
            print("Mouse Up")
            self.ai_game.game_stats.game_at_begin = False
            self.all_buttons.clear_button(button)
        elif mouse == pygame.MOUSEBUTTONDOWN:
            for i in range(3):
                button.button_color[i] *= 1.5
                if button.button_color[i] > 255:
                    button.button_color[i] = 255
            button.prep_msg(button.msg)
