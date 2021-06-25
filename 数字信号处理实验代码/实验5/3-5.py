from thinkdsp import Chirp
from thinkdsp import normalize, unbias
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate

PI2 = 2 * np.pi
class TromboneGliss(Chirp):
    
    def evaluate(self, ts):

        l1, l2 = 1.0 / self.start, 1.0 / self.end
        lengths = np.linspace(l1, l2, len(ts))
        freqs = 1 / lengths
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        ys = self.amp * np.cos(phases)
        return ys


low = 262
high = 349
signal = TromboneGliss(high, low)
wave1 = signal.make_wave(duration=1)
wave1.apodize()
wave1.make_audio()
sp1 = wave1.make_spectrogram(1024)
sp1.plot(high=1000)
#sd1 = sp1.make_wave()
#sd1.write(filename='C3_F3.wav')

signal = TromboneGliss(low, high)
wave2 = signal.make_wave(duration=1)
wave2.apodize()
wave2.make_audio()
sp2 = wave2.make_spectrogram(1024)
sp2.plot(high=1000)
#sd2 = sp2.make_wave()
#sd2.write(filename='F3_C3.wav')
#decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
#plt.show()
wave = wave1 | wave2
wave.make_audio()
sp = wave.make_spectrogram(1024)
sp.plot(high=1000)
sd = sp.make_wave()
sd.write(filename='F3_C3_C3_F3.wav')
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()