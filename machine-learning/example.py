import numpy
from scipy import stats


# Mean: The average of all the values
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print("average speed is: ", x)

# Median: The middle value of the list
speed = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]
x = numpy.median(speed)
print("mid value of spped is: ", x)

# Mode: The most common value in the list
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print("most appears value of speed is: ", x)

# Standard Deviation: The distance of all the values from the mean
speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)
y = numpy.mean(speed)

print("standard deviation is: ", x)
print("mean is: ", y)
print("meaning that most of the value are within the range of {} from the mean value, which is {}".format(x, y))

# Variance: The distance of all the values from the mean squared

x = numpy.var(speed)
print("variance is: ", x)

# Percentile: The value that is a certain percentage of the list
