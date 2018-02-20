"""
Wind Statistics
----------------

Topics: Using array methods over different axes, fancy indexing.

1. The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71

   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.

   Use the 'loadtxt' function from numpy to read the data into
   an array.

2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds over all the locations and all the times (a single set of numbers
   for the entire dataset).

3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)

4. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)

5. Find the location which has the greatest windspeed on each day (an integer
   column number for each day).

6. Find the year, month and day on which the greatest windspeed was recorded.

7. Find the average windspeed in January for each location.

You should be able to perform all of these operations without using a for
loop or other looping construct.

Bonus
~~~~~

1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (hint: first find a
   way to create an identifier unique for each month. The second step might
   require a for loop.)

2. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds across all locations for each week (assume that the first week
   starts on January 1 1961) for the first 52 weeks. This can be done without
   any for loop.

Bonus Bonus
~~~~~~~~~~~

Calculate the mean windspeed for each month without using a for loop.
(Hint: look at `searchsorted` and `add.reduceat`.)

Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.


See :ref:`wind-statistics-solution`.
"""

from numpy import loadtxt, min, max, mean, std, argmax, where
import numpy as np
import os
YEAR=0
MONTH=1
DAY=2
LOC1=3

root=os.path.dirname(__file__)
file_name='wind.data'
file_path=os.path.join(root,file_name)
wind_statistics=loadtxt(file_path, dtype=float)


print("All locations & days")
print("The minimum windspeed was {}".format(wind_statistics[:,LOC1:].min()))
print("The maximum windspeed was {}".format(wind_statistics[:,LOC1:].max()))
indexOfMax = np.unravel_index(wind_statistics[:,LOC1:].argmax(),wind_statistics.shape)[0]
print("It was recorded {:.0f}-{:.0f}-{:.0f}".format(wind_statistics[indexOfMax,MONTH],wind_statistics[indexOfMax,DAY],wind_statistics[indexOfMax,YEAR]))
print("The mean of the windspeeds was {}".format(wind_statistics[:,LOC1:].mean()))
print("The standard deviaton of the windspeeds was {}\n".format(wind_statistics[:,LOC1:].std()))

print("Each location & all days")
print("The minimum windspeeds were {}".format(wind_statistics[:,LOC1:].min(axis=0)))
print("The maximum windspeeds were {}".format(wind_statistics[:,LOC1:].max(axis=0)))
print("The means of the windspeeds were {}".format(wind_statistics[:,LOC1:].mean(axis=0)))
print("The standard deviatons of the windspeeds were {}\n".format(wind_statistics[:,LOC1:].std(axis=0)))


print("All locations & each day")
print("The minimum windspeeds were {}".format(wind_statistics[:,LOC1:].min(axis=1)))
print("The maximum windspeeds were {}".format(wind_statistics[:,LOC1:].max(axis=1)))
print("The means of the windspeeds were {}".format(wind_statistics[:,LOC1:].mean(axis=1)))
print("The standard deviatons of the windspeeds were {}\n".format(wind_statistics[:,LOC1:].std(axis=1)))

print("Location with the greatest windspeed each day {}\n".format(wind_statistics[:,LOC1:].argmax(axis=1)))

maskJanuary = wind_statistics[:,MONTH]==1
print("The means of the windspeeds for each location in January were {}".format(wind_statistics[maskJanuary,LOC1:].mean(axis=0)))

#Bonus

avg_windspeed_permonth=[]
months = np.unique(wind_statistics[:,np.array([YEAR,MONTH])],axis=0, return_index=True)

first_day=0
for last_day in months[1][1:]:
    avg_windspeed_permonth.append(wind_statistics[first_day:last_day,LOC1:].mean())
    first_day=last_day
print("The average windspeeeds for each month were {}/n".format(avg_windspeed_permonth))


   
maskYear1 = wind_statistics[:,YEAR]==wind_statistics[0,0]
print("The min of the windspeeds for each week in the first 52 weeks were {}/n".format(wind_statistics[maskYear1,LOC1:].min(axis=1)))   
print("The max of the windspeeds for each week in the first 52 weeks were {}/n".format(wind_statistics[maskYear1,LOC1:].max(axis=1)))   

print("The means of the windspeeds for each week in the first 52 weeks were {}/n".format(wind_statistics[maskYear1,LOC1:].mean(axis=1)))   
print("The standard deviations of the windspeeds for each week in the first 52 weeks were {}".format(wind_statistics[maskYear1,LOC1:].std(axis=1)))   
   
   


months = np.unique(wind_statistics[:,np.array([YEAR,MONTH])],axis=0, return_index=True)[1]
tot_windspeed_month_loc=np.add.reduceat(wind_statistics[:,LOC1:],months)
tot_windspeed_month=np.sum(tot_windspeed_month_loc,axis=1)/12
days_per_month=np.append(months[1:],(wind_statistics.shape[0]))-months #this works if windspeed isn't recorded everyday
#days_per_month=np.append(wind_statistics[months[1:]-1,DAY],wind_statistics[-1:,DAY]) #more readable?
avg_windspeed_month=tot_windspeed_month/days_per_month
print("The average windspeed each month is {}".format(avg_windspeed_month))




