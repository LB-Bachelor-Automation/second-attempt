from datavask_funksjoner import get_filepath, set_filepath, load_svg_file, create_directory
from pandas import DataFrame

acceleration:DataFrame
gyroscope:DataFrame
compass:DataFrame
fusion:DataFrame

name:str

f:str = get_filepath()
try:
    svg = load_svg_file(f,";")
    acceleration = svg[["dt", "accelX", "accelY", "accelZ"]].copy()
    gyroscope = svg[["dt", "gyroX", "gyroY", "gyroZ"]].copy()
    compass = svg[["dt", "compassX", "compassY", "compassZ"]].copy()
    fusion = svg[["dt", "fusionPoseX", "fusionPoseY", "fusionPoseZ"]].copy()
except Exception:
    svg = load_svg_file(f,",")
    acceleration = svg[["dt", "accelX", "accelY", "accelZ"]].copy()
    gyroscope = svg[["dt", "gyroX", "gyroY", "gyroZ"]].copy()
    compass = svg[["dt", "compassX", "compassY", "compassZ"]].copy()
    fusion = svg[["dt", "fusionPoseX", "fusionPoseY", "fusionPoseZ"]].copy()
    
i = f.rfind("/")
name = f[i + 1:-4]

filplassering = set_filepath(text=name)

create_directory(filplassering)

acceleration.to_csv(f"{filplassering}/acceleration")
gyroscope.to_csv(f"{filplassering}/gyroscope")
compass.to_csv(f"{filplassering}/compass")
fusion.to_csv(f"{filplassering}/fusion")