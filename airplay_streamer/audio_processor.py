## audio_processor.py
import subprocess
from pydub import AudioSegment
from typing import Optional

class AudioProcessor:
    def __init__(self, config: dict):
        self.config = config
        self.audio: Optional[AudioSegment] = None
        self.process: Optional[subprocess.Popen] = None

    def start_streaming(self) -> None:
        """
        Start streaming audio using the shairport-sync command.
        """
        command = [
            'shairport-sync',
            '-o',
            'stdout',
            '--',
            '-f',
            self.config['audio_format'],
            '-b',
            self.config['audio_bitrate'],
            '-c',
            self.config['audio_channels'],
            '-r',
            self.config['audio_rate'],
        ]
        self.process = subprocess.Popen(command, stdout=subprocess.PIPE)
        self.audio = AudioSegment.from_file(self.process.stdout, format=self.config['audio_format'])

    def stop_streaming(self) -> None:
        """
        Stop the audio streaming process.
        """
        if self.process:
            self.process.terminate()
            self.process = None
            self.audio = None
