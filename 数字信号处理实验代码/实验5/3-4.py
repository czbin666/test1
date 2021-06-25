from thinkdsp import read_wave
from thinkdsp import decorate
import matplotlib.pyplot as plt

wave = read_wave('72475__rockwehrmann__glissup02.wav')
wave.make_audio()
wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()
