# 1.) Make a data set for a linear function with bias.
# 2.) Perform regression to obtain the best fit line for this data set.
# 3.) The best fit line should like the linear function without bias
# 4.) If you would like, try doing a regression on a quadratic function after by following the same steps

import random
import matplotlib.pyplot as plt
from functools import reduce
import numpy as np
from decimal import Decimal, ROUND_HALF_UP


# def linear_function(x):
#     y =  (3 * x + 2) + bias_function(1,20)
#     return y
#
# # Random
# def bias_function( lower_boundary, higher_boundary):
#     return (random.randint(lower_boundary, higher_boundary))
#
# def get_slope_two_points(x1,y1,x2,y2):
#     m = (y2 - y1) / (x2 - x1)
#     roundup = round(m,2)
#     return roundup

def get_mean(arr_points):
    total = get_sumatory(arr_points)
    mean = total / float(len(arr_points))
    return mean

def get_variance(arr_points):
    mean = get_mean(arr_points)
    variance = 0.0
    for x in arr_points:
        variance += ((x - mean) ** 2)
    return variance

def get_covariance(x_points, y_points):
    x_mean = get_mean(x_points)
    y_mean = get_mean(y_points)
    total = 0
    i = 0
    while i < len(x_points):
        total += ((x_points[i] - x_mean) * (y_points[i] - y_mean)) / len(x_points)
        i+=1

    return total

def get_coeficients(data_set):
    h = {}
    x_points = []
    y_points = []

    print data_set

    for row in data_set:
        x_points.append(row[0])
        y_points.append(row[1])


    x_mean = get_mean(x_points)
    y_mean = get_mean(y_points)

    total = 0
    i = 0
    while i < len(x_points):
        total += get_covariance(x_points,y_points) / get_variance(x_points)
        i+=1

    m = total

    # get coeficient b
    b = y_mean - m * x_mean

    h["b"] = b
    h["m"] = m

    return h

def get_sumatory(arr_points):
    sumatory = reduce((lambda total, num: total + num), arr_points)
    return sumatory


def simple_linear_regression(train, test):
    prediction = []
    h = get_coeficients(train)
    m = h['m']
    b = h['b']

    print "------------ coeficient M -------"
    print m
    print "------------ coeficient B -------"
    print b

    for row in test:
        yhat = m * row[0] + b
        prediction.append(yhat)
    return prediction


train = [[108,392.5],[19,46.2],[13,15.7],[124,422.2],[40,119.4],[57,170.9],[23,56.9],[14,77.5],[45,214],[10,65.3],[5,20.9],[48,248.1],[11,23.5],[23,39.6],[7,48.8],[2,6.6],
         [24,134.9],[6,50.9],[3,4.4],[23,136],[20,14.8],[9,48.7],[9,52.1],[3,13.2],[29,103.9],[7,77.5],[4,11.8],[20,98.1],[7,27.9],[4,38.1],[10,25],[15,69.2],[6,14.6],[5,40.3],
         [22,161.5],[11,57.2],[61,217.6],[12,58.1],[4,12.6],[16,59.6],[13,89.9],[60,202.4],[41,181.3],[37,152.8],[55,162.8],[41,73.4],[11,21.3],[27,92.6],[8,76.1],
         [3,39.9],[17,142.1],[13,93],[23,31.9],[15,32.1],[8,55.6],[29,133.3],[30,194.5],[24,137.9],[9,87.4],[31,209.8],[14,95.5],[53,244.6],[26,187.5]]

prediction = simple_linear_regression(train,train)
#
print "----------- prediction --------------"
print prediction
print "-------------------------"
#
y_points = []
x_points = []

for row in train:
    x_points.append(row[0])
    # Plot the data
    y_points.append(row[1])

plt.scatter(x_points, y_points, color='red', marker='^')
plt.scatter(x_points, prediction, color='blue', marker='^')

# # Show the plot
plt.show()
