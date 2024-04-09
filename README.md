# Soft body simulation

Soft-body dynamics is a field of computer graphics that focuses on visually realistic physical simulations of the motion and properties of deformable objects (or soft bodies).[1] The applications are mostly in video games and films. Unlike in simulation of rigid bodies, the shape of soft bodies can change, meaning that the relative distance of two points on the object is not fixed. 

In this program, the lack of animation at the edges of the flag is presented. This shows how the model is plastic, difficult to animate, features a simple structure and must have a good physical model.

## Libraries
`numpy as np` for operations on arrays and arrays.

`matplotlib.pyplot as plt` for creating graphs.

`mpl_toolkits.mplot3d` and `Axes3D` to create 3D charts.


## Simulation parameters

`p_number_x, p_number_y`: number of points in the grid on the X and Y axes, representing the flag.

`l_flag, h_flag`: dimensions of the flag on the X (length) and Y (height) axes.

`wind_amp, wind_freq`: amplitude and frequency of the wind.

`dt`: time step of the simulation.

`num_frames`: number of frames for simulation.

## Flag grid

`x, y`: vectors representing points along the X and Y axes of the flag.

`X, Y`: coordinate matrices of points on the flag grid.

`Z`: matrix initialized with zeros, representing the initial position of the flag (flat flag)

## Simulate 

Simulates the tension of the flag material. For each point on the flag (except the edges), the new position is the average of the positions of the four neighboring points. The edges of the flag are immobile.

## Main loop

For each simulation frame:

Simulates the effect of wind by adding a sinusoidal variation to the Z position, mimicking the flag waving under the influence of wind.

Calls the simulate function to update the Z position based on material tension.

Creates a figure and axes for the 3D plot, and then draws the surface of the flag using the updated Z values.

Sets the axis ranges and camera angle.



# References 
[1] Nealen, Müller, Keiser, Boxerman & Carlson (2005). "Physically Based Deformable Models in Computer Graphics". CiteSeerX 10.1.1.124.4664


 
