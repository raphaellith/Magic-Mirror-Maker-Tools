import csv
import numpy as np
import matplotlib.pyplot as plt
from queue import PriorityQueue

from matplotlib.collections import LineCollection


class VectorFieldVisualiser:
    def __init__(self):
        self.xs = None
        self.ys = None
        self.us = None
        self.vs = None

    def load_from_csv(self, filename):
        with open(filename, newline='') as csv_file:
            reader = csv.reader(csv_file)
            row_data = [list(map(lambda string: float(string), row)) for row in reader]
            self.xs, self.ys, self.us, self.vs = map(lambda ts: np.array(ts), zip(*row_data))

    def visualise(self, skip=1):
        def not_skipped(quadruple):
            return quadruple[0] % skip == quadruple[1] % skip == 0

        xs, ys, us, vs = zip(*filter(not_skipped, zip(self.xs, self.ys, self.us, self.vs)))
        lengths = np.sqrt(np.square(us) + np.square(vs))

        plt.quiver(xs, ys, us, vs, lengths)
        plt.colorbar()
        plt.show()

    def visualise_as_lens(self, show_vertices_as_dots=False, skip=1):
        plt.gca().invert_yaxis()

        def not_skipped(quadruple):
            return quadruple[0] % skip == quadruple[1] % skip == 0

        if skip == 1:
            xs, ys, us, vs = self.xs, self.ys, self.us, self.vs
        else:
            xs, ys, us, vs = zip(*filter(not_skipped, zip(self.xs, self.ys, self.us, self.vs)))


        if show_vertices_as_dots:
            plt.scatter(us, vs, s=3)
        else:
            plt.scatter(us, vs, s=0.01)

        horizontal_lines_by_y_value = dict()
        # Key: y_value
        # Priority queue: (x, (u, v)) tuples ordered by x value

        for x, y, u, v in zip(xs, ys, us, vs):
            if y not in horizontal_lines_by_y_value:
                horizontal_lines_by_y_value[y] = PriorityQueue()
            horizontal_lines_by_y_value[y].put((x, (u, v)))

        lines = []
        for y in horizontal_lines_by_y_value.keys():
            line = []
            while not horizontal_lines_by_y_value[y].empty():
                queue_item = horizontal_lines_by_y_value[y].get()
                line.append(queue_item[1])
            lines.append(line)

        plt.gca().add_collection(LineCollection(lines, linewidths=0.5))
        plt.gca().add_collection(LineCollection(np.transpose(lines, (1, 0, 2)), linewidths=0.5))

        plt.gca().set_aspect('equal', adjustable='box')

        plt.show()

