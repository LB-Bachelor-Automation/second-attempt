from pandas import read_csv

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


def get_filepath(
    title: str = "Select Raw Data File to Read",
    filetypes: list[dict[str, str]] = [("Raw Data File", ".csv")],
) -> str:
    return filedialog.askopenfilename(title=title, filetypes=filetypes)

sss = get_filepath()
svg = read_csv(sss, sep=",")
print(sss)
