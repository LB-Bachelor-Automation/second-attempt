from pandas import read_csv, DataFrame, Timedelta, Timestamp, to_datetime
from numpy import ndarray, array, eye, roll, newaxis, zeros, einsum, zeros_like, tile
from numpy.linalg import inv
from tkinter import filedialog, Tk
import os
from scipy.spatial.transform import Rotation as R


def XYZ() -> list[str]:
    return ["X","Y","Z"]

xyz = XYZ()

def get_filepath(
    title: str = "Select Raw Data File to Read",
    filetypes: list[dict[str, str]] = [("Raw Data File", ".csv")],
) -> str:
    try:
        return filedialog.askopenfilename(title=title, filetypes=filetypes)
    except Exception as e:
        print(e)

def set_filepath(
    title: str = "Select Raw Data File to Read",
    filetypes: list[dict[str, str]] = [("Raw Data File", ".csv")],
    text:str = ""
) -> str:
    try:
        return filedialog.asksaveasfilename(title=title, filetypes=filetypes, initialfile=text)
    except Exception as e:
        print(e)
    

def load_svg_file(filepath:str, sep:str = ","):
    try:
        svg = read_csv(filepath, sep=sep).drop_duplicates()
        
        reference_time:Timestamp = to_datetime(svg['timestamp'].iloc[0])
        svg["t"] = [Timedelta(time - reference_time).total_seconds() for time in to_datetime(svg['timestamp'])]
        
        
        t1:ndarray = svg["t"].to_numpy()
        t0:ndarray = roll(svg["t"].to_numpy(),1);t0[0]=0.0
        svg["dt"] = t1 - t0
        
        return svg
    
    except Exception as e:
        print(e)


def create_directory(directory_path):
    """
    This function creates a new directory at the specified path.

    Args:
        directory_path: The path of the directory to create.

    Returns:
        None
    """
    try:
        os.mkdir(directory_path)
        print(f"Directory '{directory_path}' created successfully!")
    except FileExistsError:
        print(f"Directory '{directory_path}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def get_pose_from_gyro(dataFrame:DataFrame)->DataFrame:
    dataFrame[["dposeX","dposeY","dposeZ"]] = dataFrame[["gyroX","gyroY","gyroZ"]].to_numpy() * dataFrame["dt"].to_numpy()[:,newaxis]

    for x in xyz:
        dataFrame[f"pose{x}"] = dataFrame[f"dpose{x}"].to_numpy().cumsum()

    return dataFrame

def get_absacceleration_from_pose(dataFrame: DataFrame, degrees: bool=False) -> DataFrame:
    dataFrame[[f"absAccel{x}" for x in xyz]] = einsum(
        "ijk,ik->ik",
        
        R.from_euler(
            "xyz",
            [*(dataFrame[[f"pose{x}"for x in xyz]].to_numpy())],
            degrees=degrees)
        .inv().as_matrix(),
        
        dataFrame[[f"accel{x}"for x in xyz]].to_numpy())
    
    return dataFrame


def get_abs_g_from_pose(dataFrame: DataFrame, degrees: bool=False):
    a = dataFrame[[f"absAccel{x}"for x in xyz]].to_numpy()
    g = tile(a[0,:], a.shape[0]).reshape([*a.shape])
    
    dataFrame[[f"g{x}" for x in XYZ()]] = einsum(
        "ijk,ik->ik",
        
        R.from_euler(
            "xyz",
            [*(dataFrame[[f"pose{x}"for x in xyz]].to_numpy())],
            degrees=degrees)
        .inv().as_matrix(),
        g
    )
    dataFrame[["vaccAccelX","vaccAccelY","vaccAccelZ"]] = a - g
    dataFrame[["uvaccAccelX","uvaccAccelY","uvaccAccelZ"]] = a + g

    return dataFrame

def account_for_g(
    dataFrame: DataFrame,
    accountedNameBase:str = "accAccel",
    unaccountedNameBase: str = "absAccel",
    gNameBase: str = "g",
    axes: list[str] = XYZ()
    ) -> DataFrame:
    dataFrame[[accountedNameBase+axe for axe in axes]] = dataFrame[[unaccountedNameBase+axe for axe in axes]].to_numpy() - dataFrame[[gNameBase+axe for axe in axes]].to_numpy()
    return dataFrame

def get_abs_position_from_abs_acceleration(
    dataFrame:DataFrame,
    positionColumnNameBase: str = "absPos",
    velocityColumnNameBase: str = "abdVel",
    accelerationColumnNameBase: str = "absAccel",
    axes: str | list[str] = ["X","Y","Z"],
    dtName: str = "dt"
    ) -> DataFrame:
    
    dt = dataFrame[dtName].to_numpy()
    for axe in axes:
        a = dataFrame[accelerationColumnNameBase+axe].to_numpy()
        dataFrame["d"+velocityColumnNameBase+axe] = a * dt
        dataFrame["d"+positionColumnNameBase+axe] = 0.5 * a * dt*dt + a * dt
        
        dataFrame[velocityColumnNameBase+axe] = dataFrame["d"+velocityColumnNameBase+axe].to_numpy().cumsum()
        dataFrame[positionColumnNameBase+axe] = dataFrame["d"+positionColumnNameBase+axe].to_numpy().cumsum()
    
    return dataFrame