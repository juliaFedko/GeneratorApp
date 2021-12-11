import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import scipy.signal as signal

sampling = 44100
#sampling = int(input("'Sound generator'\nSampling: "))
time = 10
#time = int(input("Length of the sound (in seconds): "))
t = np.linspace(0, time, time * sampling)

def sine(f, A):
    data = A * np.sin(2 * np.pi * f * t)
    return data

def square(f, A):
    data = A * signal.square(2 * np.pi * f * t)
    return data

def sawtooth(f, A):
    data = A * signal.sawtooth(2 * np.pi * f * t)
    return data

def triangle(f, A):
    data = A * signal.sawtooth(2 * np.pi * f * t, width=0.5)
    return data

def whitenoise(A):
    data = A * (np.random.rand(len(t)) - 0.5)
    return data

def plotting(data, title, f):
    plt.title(str(f) + "Hz " + title + " wave in a time range of 0 to 10ms")
    plt.xlabel("Time")
    plt.ylabel("Acceleration")
    plt.xlim(0, 0.01)
    plt.plot(t, data)
    plt.show()

def sound(data, file):
    audio_data = np.int16(data * 2 ** 15)
    write(file + '.wav', sampling, audio_data)


while True:

    print("What kind of wave do you want? Choose among: \n- sine\n- square\n- sawtooth\n- triangle\n- whitenoise")
    wave = input("My choice is: ")
    if wave == "whitenoise":
        A = float(input("Amplitude: "))
        data = whitenoise(A)
    else:
        A = float(input("Amplitude: "))
        f = int(input("Frequency in Hz: "))
        if wave == "sine":
            data = sine(f, A)
        elif wave == "square":
            data = square(f, A)
        elif wave == "sawtooth":
            data = sawtooth(f, A)
        elif wave == "triangle":
            data = triangle(f, A)
        else:
            print("GIVE A PROPER WAVE")
            continue

    print("Do you want to see the plot? yes/no")
    plotQuestion = input()
    if plotQuestion == "yes":
        plotting(data, wave, f)

    print("Do you want to save it into a .wav file? yes/no")
    saveQuestion = input()
    if saveQuestion == "yes":
        fileName = input("Enter the name for the new file: ")
        sound(data, fileName)
        print("Saved!")

    print("\nDo you want to continue? yes/no")
    continueQuestion = input()
    if continueQuestion == "yes":
        continue
    else:
        break