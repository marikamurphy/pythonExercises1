"""

Topics: Matplotlib line plots, scatter plots, image plots, and histograms.

0. Sample data have been created for you in each section.
1. Create the plot shown in mpl_exercise_plot.png using the following commands:
   figure()
   subplot()
   plot()
   scatter()
   corrcoef()
   imshow()
   colorbar()
   hist()
   cla()


Notes
~~~~~

Remember: You can see the syntax for any command using the "?" syntax.
The exercise is broken down into smaller sub-steps below.
If you want a more challenging exericse, try creating the plot without looking
at the sub-steps.

Bonus
~~~~~

Add some titles and axes to the plot.

"""

import numpy as np
import matplotlib.pyplot as plt

import seaborn


# Create some sample data
x1 = np.linspace(0 ,10, 100)   # generate 100 numbers between 0 and 10
y1 = np.sin(x1)                # element-wise sin of each element in x1
e1 = np.random.ranf(100) * 5.0 # generate random floats in [0.0, 5.0)
y1_noisy = y1 + e1             # make a noisy sin wave
x2 = np.linspace(0, 10, 100)   # generate 100 numbers between 0 and 10
y2 = np.sin(x2)                # element-wise sin of each element in x2
e2 = np.random.ranf(100)*3.0   # generate noise with amplitude 3.0
offset = 3.0                   # constant offset
y2_noisy = y2 + offset + e2    # make a noisy sin wav offset from the first one

# 1. Create a new figure.
plt.figure()

# 2. Create three columns and two rows of subplots and select the first one.
plt.subplot(2,3,1)
# 3. In the top, left subplot, plot y1_noisy using a line plot with black
#    triangle markers.

plt.plot(y1_noisy,'k-^')



# 4. Overwrite the top left subplot with a plot of y1_noisy using a line plot
#    with a red dashed line.
plt.cla()
plt.plot(y1_noisy,'r--')



plt.title("Noisy Sin")
plt.legend(['y1_noisy'])



# 5. In the top, middle subplot, plot y2_noisy using a line plot with
#    green circle markers.
plt.subplot(2,3,2)
plt.plot(y2_noisy,'go')



plt.title("Offset Noisy Sin")
plt.legend(['y2_noisy'])



# 6. In the top, right subplot, plot y1_noisy vs. y2_noisy using a scatter plot
#    with blue circles.
plt.subplot(2,3,3)
plt.scatter(y1_noisy,y2_noisy,c='b')



plt.title("Noisy Sin Waves")

plt.xlabel('y1_noisy')
plt.ylabel('y2_noisy')

# 7. In the bottom, left subplot, plot the histogram of (y2_noisy - y1_noisy)
plt.subplot(2,3,4)
plt.hist(y2_noisy-y1_noisy)
plt.title("Offset - Original Sin Wave")



# 8. In the bottom, middle subplot, plot the histograms side by side for
#    y1_noisy and y2_noisy (set hold to True again first).
plt.subplot(2,3,5)



plt.hist([y1_noisy,y2_noisy])
plt.title("Noisy Sin Waves")


# 9. In the bottom, right subplot, plot the correlation matrix of
#        x1, y1, e1, y1_noisy, x2, y2, e2, y2_noisy
#    as an image.
#    Hint: syntax for correlation matrix is
#        result = np.corrcoef([arr1, arr2, arr3, ...])
plt.subplot(2,3,6)

matrix = np.corrcoef([x1,y1,e1,y1_noisy,x2,y2,e2,y2_noisy] )
labels=['x1','y1','e1','y1_noisy','x2','y2','e2','y2_noisy']
x=[1,2,3,4,5,6,7]

mask = np.zeros_like(matrix)

w=seaborn.heatmap(matrix, cmap='viridis', vmax=1.0, vmin=-1.0 , mask = mask, linewidths=2.5)
w.set_xticklabels(labels,rotation=45)
w.set_yticklabels(labels[::-1],rotation=45)


plt.imshow(matrix,interpolation='none')
# 10. Add a colorbar to the subplot.


plt.title("Correlation Matrix")




# Make sure that the figure window is updated when executing this file
# as a script.
plt.show()
