import matplotlib.pyplot as plt
from pandas import read_csv, DataFrame, Timedelta, Timestamp, to_datetime
from datavask_funksjoner import *



acceleration:DataFrame
gyroscope:DataFrame
compass:DataFrame
fusion:DataFrame


f:str = get_filepath()
svg = load_svg_file(f,";")

acceleration = svg[["dt", "accelX", "accelY", "accelZ"]].copy()
gyroscope = svg[["dt", "gyroX", "gyroY", "gyroZ"]].copy()
compass = svg[["dt", "compassX", "compassY", "compassZ"]].copy()
fusion = svg[["dt", "fusionPoseX", "fusionPoseY", "fusionPoseZ"]].copy()

fig, ax = plt.subplots(ncols=2,nrows=2)

acceleration.plot(x="dt", grid=True, ax=ax[0,0], title="Accelerometer", xlabel="seconds [s]", ylabel="g [9.81 m/s^2]")
gyroscope.plot(x="dt", grid=True, ax=ax[0,1], title="Gyroscope", xlabel="seconds [s]", ylabel="radians per second [rad/s]")
compass.plot(x="dt", grid=True, ax=ax[1,0], title="Magnetometer", xlabel="seconds [s]", ylabel="magnetic force [μT]")
fusion.plot(x="dt", grid=True, ax=ax[1,1], title="FusionPose", xlabel="seconds [s]", ylabel="unknown")
plt.show()