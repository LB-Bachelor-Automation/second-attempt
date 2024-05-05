#import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

# from matplotlib.pyplot import Axes
from typing import List
from numpy import arange, ndarray
from pandas import DataFrame
from os.path import abspath
from PolyPlot import PolyPlot
from Plot import Plot
from functionality import load, preProcess
from directoryControl import directoryControl
directoryControl()


path = abspath("/datafiles/testb2.csv"[1:])

t = "t"
dt = "dt"

data: DataFrame
cols: List[str]
raw_data, columns = load(path, sep=";")
raw_data[columns[1:]] = raw_data[columns[1:]] * 9.81
data, cols = preProcess(
    raw_data[:400],
    timestampColumnName=columns[0],
    format='%Y-%m-%dT%H:%M:%S.%fZ'
)

axis:List[str] = ["X","Y","Z"]

plots:List[Plot] = [
    # PolyPlot(
    #     xset= [data[t]],
    #     yset=[data[cols[1]]],
    #     labels=[f"X axis"],
    #     colors=["blue"],
    #     xticks=arange( start=0, stop=data[t].max(), step=1 ),
    #     yticks=arange( start=-30, stop=10, step=5 )
    # ),
    # PolyPlot(
    #     xset= [data[t]],
    #     yset=[data[cols[2]]],
    #     labels=[f"Y axis"],
    #     colors=["blue"],
    #     xticks=arange( start=0, stop=data[t].max(), step=1 ),
    #     yticks=arange( start=-30, stop=10, step=5 )
    # ),
    # PolyPlot(
    #     xset= [data[t]],
    #     yset=[data[cols[3]]],
    #     labels=[f"Z axis"],
    #     colors=["blue"],
    #     xticks=arange( start=0, stop=data[t].max(), step=1 ),
    #     yticks=arange( start=-60, stop=10, step=5 )
    # )
    PolyPlot(
        xset= [data[t]]*3,
        yset=[data[cols[1]],data[cols[2]],data[cols[3]]],
        labels=[f"X axis",f"Y axis",f"Z axis"],
        colors=["blue","green","red"],
        xticks=arange( start=0, stop=data[t].max(), step=1 ),
        yticks=arange( start=-70, stop=41, step=5 )
    )
]

subpart = "shaking"
title = f"Acceleration_{subpart}"
fig, axs = plt.subplots(ncols=1, nrows=len(plots), num=title)
fig.suptitle(subpart)

if isinstance(axs, ndarray):
    for (ax, plot) in zip(axs, plots):
        plot.plot(ax)
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Acceleration [m/s^2]")

else:
    ax = axs
    plot = plots[0]

    plot.plot(ax)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Acceleration [m/s^2]")

plt.tight_layout()
plt.show()
fig.tight_layout()
plt.tight_layout()
