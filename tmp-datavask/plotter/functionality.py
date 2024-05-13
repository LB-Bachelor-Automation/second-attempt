from typing import List
from numpy import diff, mean
from pandas import DataFrame, Timedelta, read_csv, to_datetime
from scipy.fft import fft, rfftfreq
from os.path import abspath


def load(path:str, sep:str=",") -> tuple[DataFrame, List[str]]:
    file = abspath(path)
    data = read_csv(file, sep=sep)
    return data, data.columns.to_list()

def preProcess(data:DataFrame,
        timestampColumnName:str = "timestamp",
        t:str="t",
        dt:str="dt",
        unit:str=None,
        format:str=None
) -> tuple[DataFrame,List[str]]:
    
    if unit is not None:
        data[timestampColumnName] = to_datetime(data[timestampColumnName], unit="ms")
    elif format is not None:
        data[timestampColumnName] = to_datetime(data[timestampColumnName], format='%Y-%m-%dT%H:%M:%S.%fZ')
    else:
        data[timestampColumnName] = to_datetime(data[timestampColumnName])

    data[dt] = data[timestampColumnName].diff().fillna(Timedelta(seconds=0))
    data[dt] = data[dt].dt.total_seconds()
    data[t] = data[dt].cumsum()

    return data, data.columns.to_list()

def perform_fft_analysis(data: DataFrame, columns_to_analyze: List[int]):
    t:str = 't'
    fft_results = []
    frequencies = None

    # Perform FFT analysis for each column
    for column_index in columns_to_analyze:
        column = data.iloc[:, column_index].values
        fft_result = fft(column)
        fft_results.append(fft_result)

        if frequencies is None:
            # Calculate frequencies only once using the first column
            sampling_rate = 1 / mean(diff(data[t].values))
            n = len(column)
            frequencies = rfftfreq(n, d=1/sampling_rate)

    return fft_results, frequencies