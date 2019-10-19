import pyaudio
from pydub import AudioSegment
from pydub.utils import make_chunks


class SoundPlay:
    def __init__(self):
        pass

    # 初期起動
    def wakeUp(self, filePath):
        CHUNK = 1024
        # 音源ファイル読み込み
        audio_data = AudioSegment.from_ogg(filePath)
        p = pyaudio.PyAudio()
        self.stream = p.open(format=p.get_format_from_width(audio_data.sample_width),
                        channels=audio_data.channels,
                        rate=audio_data.frame_rate,
                        output=True)
        # モジュール設定
        self.module = p
        self.audio_data = audio_data
        self.play()

    def play(self):
        for chunk in make_chunks(self.audio_data, 500):
            self.stream.write(chunk._data)
        self.stream.stop_stream()
        self.stream.close()
        self.module.terminate()
