from pathlib import Path
import json


class Settings:
    """设置类"""

    def __init__(self):
        """初始化游戏设置"""
        self.config_path = Path('config.json')
        self.config = {}

        if self.config_path.exists():
            with open(self.config_path, "r") as f:
                self.config = json.load(f)
        else:
            self.config['screen_width'] = 1920
            self.config['screen_height'] = 1080
            self.config['bg_color'] = (230, 230, 230)
            self.config['refresh_rate'] = 240
            self.config['caption'] = "Alien Invasion"

            with open(self.config_path, "w") as f:
                json.dump(self.config, f, indent=4)


