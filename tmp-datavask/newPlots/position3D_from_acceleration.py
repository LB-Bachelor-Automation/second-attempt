from subfunctions.file_reader import get_filepath
from subfunctions.PolyPlot import PolyPlot
from subfunctions.functionality import load, preProcess

from pandas import DataFrame


filepath = get_filepath()

data: DataFrame
cols: list[str]

raw_data, columns = load(filepath, sep=";")

raw_data[columns[1:]] = raw_data[columns[1:]] * 9.81

data, cols = preProcess(
    raw_data[:400], timestampColumnName=columns[0], format="%Y-%m-%dT%H:%M:%S.%fZ"
)
