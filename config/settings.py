from pathlib import Path
import json
from config.extern_var import *


class Settings:
    """设置类"""

    def __init__(self, update=False):
        """初始化游戏设置"""
        self.config_path = Path('config/config.json')
        self.config = {}

        if self.config_path.exists() and not update:
            with open(self.config_path, "r") as f:
                self.config = json.load(f)
            self.check_config()
        else:
            self.write_config()

        print("\nConfigure:")
        for conf, value in self.config.items():
            print(f"{conf}: {value}")
        print("\n")

        if not self.config['fullscreen']:
            self.config['one_x'] = self.config['screen_width'] / 1000
            self.config['one_y'] = self.config['screen_height'] / 1000

    def write_config(self):
        self.config['screen_width'] = 1920
        self.config['screen_height'] = 1080
        self.config['bg_color'] = (227, 232, 246)
        self.config['refresh_rate'] = 240
        self.config['caption'] = "Alien Invasion"
        self.config['ship_speed'] = 5
        self.config['fullscreen'] = True
        self.config['bullet_color'] = (60, 60, 60)
        self.config['bullet_speed'] = 10.0
        self.config['bullet_width'] = 10
        self.config['bullet_height'] = 30
        self.config['bullet_max'] = 100
        self.config['bullet_interval'] = 0.05  # second
        self.config['alien_init_row'] = 5
        self.config['alien_init_col'] = 10
        self.config['alien_init_cover_rate'] = 0.6
        self.config['alien_init_lr_speed'] = 0.5  # 左右移动速度
        self.config['alien_init_down_speed'] = 10     # 碰壁一次向下移动的等效速度值
        self.config['alien_init_direction'] = RIGHT_FORWARD
        self.config['alien_lr_speed_time_up'] = 0.1     # per second
        self.config['alien_lr_speed_time_max'] = 5   # times of the initial speed because of time
        self.config['alien_lr_speed_num_up'] = 0.1     # per second
        self.config['alien_lr_speed_num_max'] = 5   # times of the initial speed because of num
        self.config['alien_down_speed_time_up'] = 0.05  # per alien
        self.config['alien_down_speed_time_max'] = 2  # times of the initial speed because of time
        self.config['alien_down_speed_num_up'] = 0.05  # per alien
        self.config['alien_down_speed_num_max'] = 2  # times of the initial speed because of num

        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=4)

    def check_config(self):
        check_set = {'screen_width', 'screen_height', 'bg_color',
                     'refresh_rate', 'caption', 'ship_speed',
                     'fullscreen', 'bullet_color', 'bullet_speed',
                     'bullet_width', 'bullet_height', 'bullet_max',
                     'bullet_interval', 'alien_init_row', 'alien_init_col',
                     'alien_init_cover_rate', 'alien_init_lr_speed', 'alien_init_down_speed',
                     'alien_init_direction', 'alien_lr_speed_time_up', 'alien_lr_speed_time_max',
                     'alien_lr_speed_num_up', 'alien_lr_speed_num_max', 'alien_lr_speed_time_up',
                     'alien_lr_speed_time_max', 'alien_lr_speed_num_up', 'alien_lr_speed_num_max',
                     'alien_down_speed_time_up', 'alien_down_speed_time_max', 'alien_down_speed_num_up',
                     'alien_down_speed_num_max'}
        config_set = set(self.config.keys())
        if config_set == check_set:
            pass
        else:
            self.write_config()


if __name__ == '__main__':
    Settings(True)
