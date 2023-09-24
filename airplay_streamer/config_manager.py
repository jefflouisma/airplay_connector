import json
import os
from typing import Dict

class ConfigManager:
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = config_file
        self.config: Dict[str, str] = {}

    def load_config(self) -> None:
        """
        Load the configuration from the config file.
        If the file does not exist, create a default configuration.
        """
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
        else:
            self.config = self.default_config()
            self.save_config()

    def save_config(self) -> None:
        """
        Save the current configuration to the config file.
        """
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

    @staticmethod
    def default_config() -> Dict[str, str]:
        """
        Return the default configuration.
        """
        return {
            'audio_format': 'mp3',
            'audio_bitrate': '192k',
            'audio_channels': '2',
            'audio_rate': '44100',
            'streaming_port': '5000'
        }
