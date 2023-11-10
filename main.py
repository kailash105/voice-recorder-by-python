import numpy
import sounddevice as sd
import soundfile as sf
from tkinter import *


def voice_record():
    duration = 5
    sf = 48000
    my_recording = sd.rec(int(duration * sf), samplerate=sf, channels=2)

    sd.wait()

    return sf.write("voice_recording1.flac", my_recording, sf)


k = Tk()

Label(k, text=" voice recorder :").grid(row=0, sticky=W, rowspan=5)

b = Button(k, text="start", command=voice_record)
b.grid(row=5, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
