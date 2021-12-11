import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import scipy.signal as signal
import pandas as pd

class Generator():

    def __init__(self):
        self.time = 5
        self.sampling = 44100
        self.f = 440
        self.A = 1
        self.type = "sine"


    def sine(self):
        self.t = np.linspace(0, self.time, self.time * self.sampling)
        self.data = self.A * np.sin(2 * np.pi * self.f * self.t)
        data = {"t": self.t, "y": self.data}
        dataframe = pd.DataFrame(data)
        return dataframe

    def square(self):
        self.data = self.A * signal.square(2 * np.pi * self.f * self.t)
        return self.data

    def sawtooth(self):
        self.data = self.A * signal.sawtooth(2 * np.pi * self.f * self.t)
        return self.data

    def triangle(self):
        self.data = self.A * signal.sawtooth(2 * np.pi * self.f * self.t, width=0.5)
        return self.data

    def whitenoise(self):
        self.data = self.A * (np.random.rand(len(self.t)) - 0.5)
        return self.data

    def plotting(self):
        plt.title(str(self.f) + "Hz " + self.type + " wave in a time range of 0 to 10ms")
        plt.xlabel("Time")
        plt.ylabel("Acceleration")
        plt.xlim(0, 0.01)
        plt.plot(self.t, self.data)
        plt.show()

    def sound(self, data, file):
        audio_data = np.int16(data * 2 ** 15)
        write(file + '.wav', self.sampling, audio_data)
