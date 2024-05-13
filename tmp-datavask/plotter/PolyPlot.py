
from typing import List
from matplotlib.axes import Axes
from numpy import dtype

from Plot import Plot, generate_random_colors


class PolyPlot(Plot):
    def __init__(
        self,
        xset: List[dtype],
        yset: List[dtype],
        colors: List[str] = None,
        labels: List[str] = None,
        xticks: List[int | float] = None,
        yticks: List[int | float] = None,
    ) -> None:
        
        if colors is None:
            colors = generate_random_colors(len(yset))

        elif len(colors) < len(yset):
            colors.append(generate_random_colors(len(yset)-len(colors)))

        super().__init__(
            x=xset[0],
            y=yset[0],
            label=labels[0],
            color=colors[0],
            xticks=xticks,
            yticks=yticks,
        )

        self.xset: List[dtype] = xset
        self.yset: List[dtype] = yset

        self.colors: List[str] = colors
        self.labels: List[str] = labels
        self.xticks: List[int | float] = xticks
        self.yticks: List[int | float] = yticks

    def plot(self, ax: Axes):
        for (x, y, color, label) in zip(self.xset, self.yset, self.colors, self.labels):
            ax.plot(x, y, label=label, color=color)
        return super().plot(ax)