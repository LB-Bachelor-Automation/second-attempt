from typing import List
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from os.path import abspath
from PolyPlot import PolyPlot

from functionality import preProcess, load, perform_fft_analysis

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

columns_to_analyze = [1, 2, 3]  # Specify the column indices to analyze

np_columns = data.iloc[:, columns_to_analyze].values

fft_results, frequencies = perform_fft_analysis(data, columns_to_analyze)

axis = ["X", "Y", "Z"]
colors = ["blue", "green", "red"]  # Provide a list of colors for each line

labels = [f"{axis[i]} Axis" for i in range(len(columns_to_analyze))]
yset = [np.abs(fft_results[i][: len(data) // 2]) for i in range(len(columns_to_analyze))]
xset = [frequencies[: len(data) // 2] for _ in range(len(columns_to_analyze))]

plot = PolyPlot(xset=xset, yset=yset, labels=[None]*3, colors=colors)

segment = "shaking"
title = f"Fourier_acceleration_{segment}"
fig, ax = plt.subplots(num=title)
fig.suptitle(f"fourier analysis of {segment}")

plot.plot(ax)
ax.set_xlabel("Frequency [Hz]")
ax.set_ylabel("Acceleration [m/s^2]")

ax.legend(labels,loc="upper right")

plt.show()
