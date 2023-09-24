from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from typing import Dict
from .audio_processor import AudioProcessor

class WebInterface:
    def __init__(self, config: Dict[str, str], audio_processor: AudioProcessor):
        self.config = config
        self.audio_processor = audio_processor
        self.app = Flask(__name__)
        self.socketio = SocketIO(self.app)

        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/start_streaming', methods=['POST'])
        def start_streaming():
            self.audio_processor.start_streaming()
            emit('status', {'streaming': True})
            return 'Streaming started', 200

        @self.app.route('/stop_streaming', methods=['POST'])
        def stop_streaming():
            self.audio_processor.stop_streaming()
            emit('status', {'streaming': False})
            return 'Streaming stopped', 200

        @self.socketio.on('connect')
        def handle_connect():
            emit('status', {'streaming': self.audio_processor.process is not None})

        @self.socketio.on('disconnect')
        def handle_disconnect():
            pass

    def update_ui(self):
        self.socketio.emit('status', {'streaming': self.audio_processor.process is not None})

    def run(self):
        self.socketio.run(self.app, host='0.0.0.0', port=int(self.config['streaming_port']))
