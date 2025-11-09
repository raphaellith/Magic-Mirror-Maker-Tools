import numpy as np
import matplotlib.pyplot as plt

from Colormap import get_greyscale_colormap


class ScalarFieldVisualiser:
    def __init__(self):
        self.array = None
        self.width, self.height = -1, -1

    def load_from_csv(self, filename):
        self.array = np.loadtxt(fname=filename, delimiter=",")
        self.width, self.height = self.array.shape

    def visualise2d(self, greyscale=False):
        if greyscale:
            plt.imshow(self.array, cmap=get_greyscale_colormap())
        else:
            plt.imshow(self.array)

        plt.colorbar()
        plt.show()

    def visualise3d(self):
        x, y = np.meshgrid(np.arange(self.width), np.arange(self.height))
        z = self.array

        fig = plt.figure()

        ax = fig.add_subplot(projection='3d')

        ax.plot_surface(x, y, z, cmap=get_greyscale_colormap())

        plt.show()
