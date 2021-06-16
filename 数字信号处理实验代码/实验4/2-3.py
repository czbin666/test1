from thinkdsp import SquareSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np

signal = SquareSignal(1100)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(211)
segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()
spectrum = wave.make_spectrum()
plt.subplot(212)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()
#sound = spectrum.make_wave()
#sound.make_audio()
#sound.write(filename='mix1.wav') 

