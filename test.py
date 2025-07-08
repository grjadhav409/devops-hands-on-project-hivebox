import numpy as np
import matplotlib.pyplot as plt
def plot_square(x, y):
    y_squared = np.square(y)
    return plt.plot(x, y_squared)