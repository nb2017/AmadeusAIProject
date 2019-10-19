# Amadeus AI処理
import pyaudio
from pydub import AudioSegment
from pydub.utils import make_chunks
from AmadeusBase import AmadeusBase

class AmadeusSound(AmadeusBase):
    amadeusSoundFile = [
        'tm_nonsense',
        'could_i_help',
        'leskinen_oh_no',
        'ringtone_over_the_sky',
        'tm_not_possible',
        'daga_kotowaru',
        'leskinen_shaman',
        'ringtone_precaution',
        'tm_scientist_no_evidence',
        'devilish_pervert',
        'look_forward_to_working',
        'ringtone_reunion',
        'tm_too_early',
        'dont_add_tina',
        'memories_christina',
        'ringtone_village',
        'tm_we_dont_know',
        'dont_call_me_like_that',
        'memory_complex',
        'secret_diary',
        'tm_you_said',
        'gah',
        'modifying_memories_impossible',
        'senpai_please_dont_tell',
        'tone',
        'gah_extended',
        'nice,senpai_question',
        'uh_senpai',
    ]
    
    def __init__(self):
        pass
    # 初期起動
    def wakeUp(self):
        super(AmadeusSound, self).wakeUp()

        # SoundPlay().wakeUp('./py/christina.ogg')
        
        CHUNK = 1024
        # 音源ファイル読み込み
        filePath = './sound/' + self.amadeusSoundFile[9] + '.ogg'
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
