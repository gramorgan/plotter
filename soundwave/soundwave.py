from plot import Plot
import audiofile as af
import numpy as np
import math

def main(p: Plot):
    p.plot_size = 4
    p.setup()
    p.draw_bounding_box()
    num_bins = round(100/p.inches_to_units(0.02))
    audio = af.read('soundwave/caves.m4a')[0]
    # take abs to get magnitude
    audio = np.abs(audio)
    # sum to mono
    audio = np.sum(audio, axis=0)
    # pad end to nearest multiple of bin width
    pad_len = math.ceil(audio.shape[0]/num_bins)*num_bins - audio.shape[0]
    audio = np.pad(audio, (0, pad_len))
    # reshape into 2d array of bins
    audio = np.reshape(audio, (num_bins, -1))
    # sum bins to 1d array of values
    audio = np.sum(audio, axis=1)
    # normalize
    audio = audio/np.max(audio)

    max_width = 30
    for i, sample in enumerate(audio):
        x = 100*i/len(audio)
        p.goto(x, 50 + max_width*sample)
        p.lineto(x, 50 - max_width*sample)
