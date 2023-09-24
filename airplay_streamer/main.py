## main.py
from .audio_processor import AudioProcessor
from .web_interface import WebInterface
from .config_manager import ConfigManager

class Main:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.config_manager.load_config()

        self.audio_processor = AudioProcessor(self.config_manager.config)
        self.web_interface = WebInterface(self.config_manager.config, self.audio_processor)

    def run(self):
        self.web_interface.run()
        self.config_manager.save_config()

if __name__ == "__main__":
    main = Main()
    main.run()
