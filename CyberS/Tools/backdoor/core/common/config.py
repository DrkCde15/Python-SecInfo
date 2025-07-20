import os
import glob
from configobj import ConfigObj

class Settings:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, '..', 'config', 'app.ini')
        self.config = ConfigObj(config_path)

    def get_value(self, key):
        return self.config.get(key, None)

    def set_value(self, key, value):
        self.config[key] = value
        self.config.write()

    def get_payload_status(self, plugin_name):
        try:
            return self.config['plugin'].as_bool(plugin_name)
        except Exception:
            return False

    def set_payload_status(self, plugin_name, status):
        self.config['plugin'][plugin_name] = status
        self.config.write()