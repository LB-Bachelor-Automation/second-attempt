from numpy import dtype
from typing import List
from matplotlib.pyplot import Axes

from random import random

def generate_random_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        r = random()
        g = random()
        b = random()
        color = (r, g, b)
        colors.append(color)
    return colors

class Plot:
    def __init__(
        self,
        x: dtype,
        y: dtype,
        color: str = "blue",
        label: str = None,
        xticks: List[int | float] = None,
        yticks: List[int | float] = None,
    ) -> None:
        self.x: dtype = x
        self.y: dtype = y
        self.color: str = color
        self.label: str = label
        self.xticks: List[int | float] = xticks
        self.yticks: List[int | float] = yticks

    def plot(self, ax: Axes):
        if self.__class__.__name__ == "Plot":
            ax.plot(self.x, self.y, label=self.label, color=self.color, marker="o")

        if self.label is not None:
            ax.legend(loc="upper left")

        if self.xticks is not None:
            ax.set_xticks(self.xticks)

        if self.yticks is not None:
            ax.set_yticks(self.yticks)

        ax.grid(True)