# from pydub import AudioSegment
# from pydub.playback import play
#
# sound = AudioSegment.from_mp3('a.mp3')
# play(sound)

from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_wav('audio/music1.wav')
play(sound)