from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np



triangle = TriangleSignal(440).make_wave(duration=0.01)
triangle.plot()
decorate(xlabel='Time (s)')
spectrum = triangle.make_spectrum()
t=spectrum.hs[0]
print(t)
spectrum.hs[0] = 100
t1=spectrum.hs[0]
print(t1)
triangle.plot(color='gray')
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')
plt.show()