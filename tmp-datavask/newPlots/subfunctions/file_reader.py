import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


def get_filepath(
    title: str = "Select Raw Data File to Read",
    filetypes: list[dict[str, str]] = [("Raw Data File", ".csv")],
) -> str:
    return filedialog.askopenfilename(title=title, filetypes=filetypes)


if __name__ == "__main__":
    print(get_filepath())
