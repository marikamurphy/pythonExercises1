"""
Calculate Derivative
--------------------

Topics: NumPy array indexing and array math.

Use array slicing and math operations to calculate the
numerical derivative of ``sin`` from 0 to ``2*pi``.  There is no
need to use a 'for' loop for this.

Plot the resulting values and compare to ``cos``.

Bonus
~~~~~

Implement integration of the same function using Riemann sums or the
trapezoidal rule.

See :ref:`calc-derivative-solution`.
"""
import numpy as np
from numpy import linspace, pi, sin, cos, cumsum
import matplotlib.pyplot as plt
# calculate the sin() function on evenly spaced data.
x = np.array(linspace(0,2*pi,101))
y = np.array(sin(x))
plt.figure()

plt.subplot(2,1,1)

plt.plot(x,y)
plt.title("Sine")

derivativeOfY=(y[:-1]-y[1:])/(x[:-1]-x[1:])
newX=(x[:-1]+x[1:])/2

plt.subplot(2,1,2)

plt.plot(newX,derivativeOfY)
plt.title("Derivative of Sine")
plt.show()
