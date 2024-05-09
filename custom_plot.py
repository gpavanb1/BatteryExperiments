import matplotlib.pyplot as plt
from itertools import cycle


class CustomPlot:
    def __init__(self, solutions, labels, xaxis="Time [h]", yaxis=None):
        # Plot voltage and current profiles
        linestyles = cycle(['-', '--', ':'])  # Repeat linestyles

        # Create the QuickPlot manually
        self.fig, self.ax = plt.subplots()
        for solution, label in zip(solutions, labels):
            ls = next(linestyles)
            self.ax.plot(solution[xaxis].entries,
                         solution[yaxis].entries, label=label, linestyle=ls)

        # Customize the legend position to be at the top-right corner
        self.ax.legend(loc="upper right")
        # Set labels and title
        self.ax.set_xlabel(xaxis)
        self.ax.set_ylabel(yaxis)
        self.ax.set_xlim([0, 1])
