from scipy.interpolate import CubicSpline
import numpy as np
x=np.array([0,1,2])
y=np.array([1,2,4])
z=CubicSpline(x,y)
print ("The interpolated value using CubicSpline method is ", z(1.5))

print("The actual value of the function is ", 2**1.5)
