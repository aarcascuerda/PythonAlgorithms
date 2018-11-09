import numpy as np
import matplotlib.pyplot as plt

# These plots need matplotlib.pyplot running in the main program as well as calling the function, matplotlib.pyplot.figure() before calling them.


def drawhistogram(data, n_bins=50, normalized=True, center=0.5, err_y=True, bar_color="green", bar_width=0.1, err_color="red"):
    """Plots an histogram with pyplot.bar

    It plots an histogram given a list in data, it has many options to configure it such as error bars."""

    y, binEdges = np.histogram(data, bins=n_bins, density=normalized)
    bincenters = center*(binEdges[1:]+binEdges[:-1])
    dx = float(np.absolute(float(binEdges[0])-float(binEdges[1])))
    if err_y == True:
        err = [np.sqrt(x*dx/float(len(data))*(1-x*dx))/dx for x in iter(y)]
        plt.bar(bincenters, y, color=bar_color,
                width=bar_width, yerr=err, ecolor=err_color)
    plt.bar(bincenters, y, color=bar_color, width=bar_width)
