"""
Wind Statistics
----------------

This exercise is an alternative version of the Numpy exercise but this time we
will be using pandas for all tasks. The data have been modified to contain some
missing values, identified by NaN.  Using pandas should make this exercise
easier, in particular for the bonus question.


Of course, you should be able to perform all of these operations without using
a for loop or other looping construct.


Topics: Pandas, time-series

1. The data in 'wind.data' has the following format::

        Yr Mo Dy   RPT   VAL   ROS   KIL   SHA   BIR   DUB   CLA   MUL   CLO   BEL   MAL
        61  1  1 15.04 14.96 13.17  9.29   NaN  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71   NaN 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25   NaN  8.50  7.67 12.75 12.71

   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.

   Use the 'pd.read_table' function from pandas to read the data into
   a DataFrame.

2. Replace the first 3 columns by a proper datetime index.

3. Compute how many values are missing for each location over the entire
   record.  They should be ignored in all calculations below. Compute how many
   non-missing values there are in total.

4. Calculate the mean windspeeds of the windspeeds over all the locations and
   all the times (a single number for the entire dataset).

5. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)

6. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)

7. Find the average windspeed in January for each location.  Treat
   January 1961 and January 1962 both as January.

8. Downsample the record to a yearly, monthly and weekly frequency
   for each location.

9. Plot the time series and a box plot of the monthly data for each location.

Bonus
~~~~~

10. Calculate the mean windspeed for each month in the dataset.  Treat
    January 1961 and January 1962 as *different* months.

11. Calculate the min, max and mean windspeeds and standard deviations of the
    windspeeds across all locations for each week (assume that the first week
    starts on January 1 1961) for the first 52 weeks.

Notes
~~~~~

This solution has been tested with Pandas version 0.14.1.

The original data from which these were derived were analyzed in detail in the
following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.


See :ref:`pandas-wind-statistics-solution`.

"""

from matplotlib import pyplot as plt
import pandas as pd
import os
root = os.path.dirname(__file__)
file_name = 'wind.data'
file_path = os.path.join(root,file_name)

#parts 1&2
def wind_date_parser(year,month,day):
    
    date_str = "19{0}-{1}-{2}".format(year,month,day)
    return pd.Period(date_str, freq='D')

wind_data = pd.read_table(file_path, sep='\\s+', index_col=0, 
                            parse_dates={'Date':[0,1,2]}, 
                            date_parser=wind_date_parser)
                            
print("Windspeeds at various locations in Ireland")                            

#part 3
print("Number of missing values over each location")
num_rows_wind_data = wind_data.iloc[:,0].size
print(num_rows_wind_data-wind_data.count())

count_not_null = wind_data.count().sum()
print("Number of non-missing values in total: {0}".format(count_not_null))

#part 4
print("Mean over all locations:")
print(wind_data.mean().mean())

#part 5
print("Statistics at each location:")
print("Mins:")
print(wind_data.min())
print("Maxes:")
print(wind_data.max())
print("Means:")
print(wind_data.mean())

#part 6
print("Daily statistics:")
print("Mins:")
print(wind_data.min(axis=1))
print("Maxes:")
print(wind_data.max(axis=1))
print("Means:")
print(wind_data.mean(axis=1))

#part 7
print("Mean for January")
jan_wind_data= wind_data[wind_data.index.month == 1]
print(jan_wind_data.mean())

#part 8
print("Downsampled yearly:")
print(wind_data.resample('A').mean())
print("Downsampled monthly:")
print(wind_data.resample('M').mean())
print("Downsampled weekly:")
print(wind_data.resample('W').mean())

#part 9
monthly_wind_data = wind_data.resample('M').mean()
axes = monthly_wind_data.plot()
plt.figure()
monthly_wind_data.boxplot()
plt.show()

#part 10
print("Mean for each month, each location:")
print(wind_data.resample('M').mean().mean(axis=1))


#part 11
print("Statistics for 52 Weeks:")
week_wind_data_52 = wind_data.resample('W').mean()[:52]
week_stats_52 = pd.concat([week_wind_data_52.min(axis=1),
                            week_wind_data_52.max(axis=1),
                            week_wind_data_52.mean(axis=1)],
                            axis=1, keys=['Min','Max','Mean'])

print(week_stats_52)