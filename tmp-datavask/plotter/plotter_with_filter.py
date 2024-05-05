import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Union
#from tkinter import filedialog

import subprocess
import os
git_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
os.chdir(git_root)


import matplotlib as mpl
mpl.rcParams["savefig.directory"] = "/figures"
mpl.rcParams["savefig.format"] = "eps"


def create_subplots(num_plots: int, subPlotMargin: float) -> tuple:
    """
    Create subplots for the given number of plots and subplot margin.

    Args:
        num_plots (int): The number of plots.
        subPlotMargin (float): The margin space between subplots.

    Returns:
        tuple: A tuple containing the figure and axes objects.
    """
    fig, axs = plt.subplots(nrows=num_plots, ncols=1, figsize=(8, 3 * num_plots))
    fig.subplots_adjust(hspace=subPlotMargin)
    return fig, axs

def plot_data(ax, x_data, y_data, marker, linestyle):
    """
    Plot data on the given axis.

    Args:
        ax: The axis object.
        x_data: The x-axis data.
        y_data: The y-axis data.
        marker: The marker style.
        linestyle: The line style.
    """
    ax.plot(x_data, y_data, marker=marker, linestyle=linestyle)

def set_labels(ax, xlabel, ylabel, title):
    """
    Set labels and title for the given axis.

    Args:
        ax: The axis object.
        xlabel: The label for the x-axis.
        ylabel: The label for the y-axis.
        title: The title for the axis.
    """
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel(ylabel=ylabel)
    ax.set_title(label=title)

def set_limits(ax, ylim):
    """
    Set y-axis limits for the given axis.

    Args:
        ax: The axis object.
        ylim: The y-axis limits.
    """
    if ylim[0] is not None:
        ax.set_ylim(bottom=ylim[0])
    if ylim[1] is not None:
        ax.set_ylim(top=ylim[1])

def set_ticks(ax, data, x_columns, yTickPatterns, xTickPatterns, i):
    """
    Set ticks for the given axis.

    Args:
        ax: The axis object.
        data: The data.
        x_columns: The column names for the x-axis.
        yTickPatterns: The tick patterns for the y-axis.
        xTickPatterns: The tick patterns for the x-axis.
        i: The index of the subplot.
    """
    if yTickPatterns is not None:
        ylim = ax.get_ylim()
        y_ticks = np.arange(ylim[0], ylim[1] + yTickPatterns[i], yTickPatterns[i])
        ax.set_yticks(y_ticks)

    if xTickPatterns is not None:
        x_ticks = np.arange(min(data[x_columns[i]]), max(data[x_columns[i]]) + xTickPatterns[i], xTickPatterns[i])
        ax.set_xticks(x_ticks)

def add_legend(ax, legend):
    """
    Add legend to the given axis.

    Args:
        ax: The axis object.
        legend: The legend.
    """
    ax.legend(legend)

def display(
        data: pd.DataFrame,
        xColumns: List[str] = None,
        ySets: List[List[str]] = None,
        titles: List[str] = None,
        figname: str = None,
        legends: List[List[str]] = None,
        xLabels: List[str] = None,
        yLabels: List[str] = None,
        yLimits: List[List[Union[int, float]]] = None,
        xTickPatterns: List[Union[int, float]] = None,
        yTickPatterns: List[Union[int, float]] = None,
        subPlotMargin: float = 0.5,
) -> None:
    """
    Display the data in subplots with customizable settings.

    Args:
        data (pd.DataFrame): The input data.
        xColumns (List[str], optional): The column names for the x-axis data. Defaults to None.
        ySets (List[List[str]], optional): The list of lists of column names for the y-axis data. Defaults to None.
        titles (List[str], optional): The list of titles for each subplot. Defaults to None.
        figname (str, optional): the figure name
        legends (List[List[str]], optional): The list of lists of legends for each subplot. Defaults to None.
        xLabels (List[str], optional): The list of labels for the x-axis. Defaults to None.
        yLabels (List[str], optional): The list of labels for the y-axis. Defaults to None.
        yLimits (List[List[Union[int, float]]], optional): The list of y-axis limits for each subplot. Defaults to None.
        xTickPatterns (List[Union[int, float]], optional): The list of tick patterns for the x-axis. Defaults to None.
        yTickPatterns (List[Union[int, float]], optional): The list of tick patterns for the y-axis. Defaults to None.
        subPlotMargin (float, optional): The margin space between subplots. Defaults to 0.5.

    Returns:
        None
    """

    if not ySets:
        ySets = [data.columns.to_list()[1:]]

    num_plots = len(ySets)

    if not titles:
        titles = [f"Plot {i + 1}" for i in range(num_plots)]
    if not legends:
        legends = [[f"Graph {i + 1}" for i in range(len(ySets[i]))] for i in range(num_plots)]
    if not yLabels:
        yLabels = ["Y Axis"] * num_plots
    if not xLabels:
        xLabels = [""] * num_plots
    if not yLimits:
        yLimits = [[None, None]] * num_plots

    fig, axs = create_subplots(num_plots, subPlotMargin)

    populate_subplots(axs, num_plots, ySets, titles, xLabels, yLabels, yLimits, legends, data, xColumns, yTickPatterns, xTickPatterns)

    plt.tight_layout()
    fig.tight_layout()
    plt.show()


def populate_subplots(axs, num_plots, ySets, titles, xLabels, yLabels, yLimits, legends, data, xColumns, yTickPatterns, xTickPatterns):
    """
    Populate the subplots with data and configure settings.

    Args:
        axs (Axes or array-like of Axes): The subplot axes.
        num_plots (int): The number of subplots.
        ySets (List[List[str]]): The list of lists of column names for the y-axis data.
        titles (List[str]): The list of titles for each subplot.
        xLabels (List[str]): The list of labels for the x-axis.
        yLabels (List[str]): The list of labels for the y-axis.
        yLimits (List[List[Union[int, float]]]): The list of y-axis limits for each subplot.
        legends (List[List[str]]): The list of lists of legends for each subplot.
        data (pd.DataFrame): The input data.
        xColumns (List[str]): The column names for the x-axis data.
        yTickPatterns (List[Union[int, float]]): The list of tick patterns for the y-axis.
        xTickPatterns (List[Union[int, float]]): The list of tick patterns for the x-axis.

    Returns:
        None
    """

    for i, (ySet, title, xlabel, ylabel, ylim, legend) in enumerate(
        zip(ySets, titles, xLabels, yLabels, yLimits, legends)
    ):
        ax = axs[i] if num_plots > 1 else axs

        for yLine in ySet:
            plot_data(ax, data[xColumns], data[yLine], marker="o", linestyle="-")

        set_labels(ax, xlabel, ylabel, title)
        set_limits(ax, ylim)
        set_ticks(ax, data, xColumns, yTickPatterns, xTickPatterns, i)
        add_legend(ax, legend)

        ax.grid(True, linewidth=0.5, alpha=0.5)


def plot_data(ax, x, y, **kwargs):
    """
    Plot data on a given axes.

    Args:
        ax (Axes): The axes on which to plot the data.
        x (array-like): The x-axis data.
        y (array-like): The y-axis data.
        **kwargs: Additional keyword arguments to be passed to the plot function.

    Returns:
        Line2D: The plotted line.
    """
    line, _, _ = ax.plot(x, y, **kwargs)
    return line


def set_labels(ax, xlabel, ylabel, title):
    """
    Set the labels and title of a given axes.

    Args:
        ax (Axes): The axes for which to set the labels and title.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
        title (str): The title of the plot.

    Returns:
        None
    """
    ax.set_xlabel(xlabel=xlabel)
    ax




def load(file_path: str, sep: str = ",") -> pd.DataFrame:
    """
    # behavior
    Load data from a CSV file.

    #Args:
        - file_path (str): The path to the CSV file.
        - sep (str, optional): The separator used in the CSV file. Defaults to ",".

    # Returns:
        pd.DataFrame: The loaded data as a DataFrame.
    """
    return pd.read_csv(file_path, sep=sep)


def wash(
        data: pd.DataFrame,
        timestamp: str = "timestamp",
        zero_time:bool = False
) -> pd.DataFrame:
    """
    Preprocess the data.

    Args:
        data (pd.DataFrame): The input data.
        timestamp (str, optional): The name of the timestamp column. Defaults to "timestamp".

    Returns:
        pd.DataFrame: The preprocessed data.
    """

    dt = "dt"
    t = "t"
    
    # Convert timestamps to datetime format
    try:
        data[timestamp] = pd.to_datetime(data[timestamp], unit='ms')
    except ValueError:
        data[timestamp] = pd.to_datetime(data[timestamp], format='%Y-%m-%dT%H:%M:%S.%fZ')


    if zero_time:
        data[timestamp] = data[timestamp] - data[timestamp].min()

    data[dt] = data[timestamp].diff().fillna(pd.Timedelta(seconds=0))
    data[dt] = data[dt].dt.total_seconds()  # Convert differences to seconds
    data[t] = data[dt].cumsum()

    return data

def moving_average(data: pd.DataFrame, columns: list, window_size: int) -> pd.DataFrame:
    """
    Computes the moving average of specified columns in a DataFrame using a specified window size.
    
    Parameters:
    - data (pd.DataFrame): The input DataFrame.
    - columns (list): The list of column names for which to calculate the moving average.
    - window_size (int): The size of the moving window.
    
    Returns:
    - pd.DataFrame: The DataFrame containing the moving average values for each column.
    """
    moving_avg_data = pd.DataFrame()
    for column in columns:
        moving_avg_data[column] = data[column].rolling(window=window_size, min_periods=1, center=True).mean()
    return moving_avg_data

def fft_analysis(data: pd.DataFrame, columns: list, timestamp: str):
    """
    Perform Fourier analysis on the specified columns of a pandas DataFrame.

    Args:
        data (pd.DataFrame): The input data.
        columns (list): A list of column names to analyze.
        timestamp (str): The name of the timestamp column.

    Returns:
        dict: A dictionary containing the frequency and amplitude data for each column.
    """
    results = {}

    for col in columns:
        # Get the data from the specified column
        x = data[timestamp].values
        y = data[col].values

        # Perform Fourier analysis
        sample_rate = 1 / np.mean(np.diff(x))
        frequencies = np.fft.fftfreq(len(x), d=1 / sample_rate)
        amplitudes = np.abs(np.fft.fft(y))

        # Store the frequency and amplitude data in the results dictionary
        results[col] = {
            'frequency': frequencies,
            'amplitude': amplitudes
        }

    return results

if __name__ == "__main__":
    file_path = "datafiles/Acceleration control tests sifter - Control test 1.csv"

    raw_data = load(file_path, sep=",")

    #print ( raw_data )
    columns = raw_data.columns.to_list()
    data = wash(raw_data[20:], columns[0], zero_time=True)

    #g = 9.81  # m/s^2
    g = 1  # m/s^2
    columns = data.columns.to_list()
    data[columns[1:]] = data[columns[1:]] * g
    columns = data.columns.to_list()
    
    start=0
    stop=400

    data_chunk = data[start:stop]

    window_size = 5

    moving_avg_data = moving_average(
        data_chunk,
        columns[1:],
        window_size)

    display(
        data=moving_avg_data ,
        xColumns=["t"] * 3,
        ySets=[([columns[i]]) for i in range(1,4)],
        titles=[
            "Acceleration X Axis",
            "Acceleration Y Axis",
            "Acceleration Z Axis"
        ],
        figname="prototype test b1",
        legends=[
            ["X Axis"],
            ["Y Axis"],
            ["Z Axis"]
        ],
        xLabels=["Time (s)"] * 3,
        yLabels=["Acceleration (m/s^2)"] * 3,
        yLimits=[[-80, 40]] * 3,
        xTickPatterns=[5] * 3,
        yTickPatterns=[7.5] * 3,
    )
