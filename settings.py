from pathlib import Path
import json


class Settings:
    """设置类"""

    def __init__(self, update=False):
        """初始化游戏设置"""
        self.config_path = Path('config.json')
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
        self.config['ship_speed'] = 1.5
        self.config['fullscreen'] = True
        self.config['bullet_color'] = (60, 60, 60)
        self.config['bullet_speed'] = 3.0
        self.config['bullet_width'] = 3
        self.config['bullet_height'] = 15
        self.config['bullet_max'] = 5
        self.config['bullet_interval'] = 0.2  # second

        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=4)

    def check_config(self):
        check_set = {'screen_width', 'screen_height', 'bg_color',
                     'refresh_rate', 'caption', 'ship_speed',
                     'fullscreen', 'bullet_color', 'bullet_speed',
                     'bullet_width', 'bullet_height', 'bullet_max',
                     'bullet_interval'}
        config_set = set(self.config.keys())
        if config_set == check_set:
            pass
        else:
            self.write_config()


if __name__ == '__main__':
    Settings(True)
