# The new plots' folder

The new "plots" folder is containing software to read the raw data and graphing it.

## Valuable locations

| name                                                                                   | description                                                    |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------|
| [sub functions](/datavask/newPlots/subfunctions/)                                      | the folder containing functions to be imported                 |
| [position in 3D from acceleration](/datavask/newPlots/position3D_from_acceleration.py) | plot position in 3d from raw data                              |

## Units from the sensors

| sensor       | unit      | etc.                           |
| ------------ | --------- | ------------------------------ |
| Acceleration | [G]       | multiple of 9.81 [m/s^2]       |
| Gyroscope    | [rad/s]   | radians per second             |
| Compass      | [μT]      | micro Tesla                    |
| FusionPose   | [unknown] | sensor pose from IMU fusion    |
| TiltHeading  | [unknown] | information unknown            |
| Pressure     | [mBar]    | milliBar air pressure          |
| Temperature  | [°C]      | will read internal heating     |
| Humidity     | [%]       | the air humidity in percentage |
