from plot import Plot
import audiofile as af
import numpy as np

def main(p: Plot):
    p.plot_size = 4
    p.setup()
    p.draw_bounding_box()
    num_bins = round(100/p.inches_to_units(0.02))
    audio = af.read('./caves.m4a')[0]
    audio = np.average(audio, axis=0)
    audio = audio[:audio.shape[0]-audio.shape[0]%num_bins]
    audio = np.abs(audio)
    audio = np.reshape(audio, (num_bins, -1))
    audio = np.average(audio, axis=1)
    audio = audio/np.max(audio)

    max_width = 10
    for i, sample in enumerate(audio):
        x = 100*i/len(audio)
        p.goto(x, 50 + max_width*sample)
        p.lineto(x, 50 - max_width*sample)

if __name__ == '__main__':
    main(None)