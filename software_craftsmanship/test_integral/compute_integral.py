""" This is a supporting module for the test_integral exercise. For a
description of this exercise, refer to the file test_integral.py.
"""

from __future__ import print_function
from numpy import array, linspace, sum, ones


def integrator(func, a, b, precision=100.):
    """ Compute the definite integral of a given function func between a and b
    using the rectangle method.
    """
    if a==b:
        return 0
    x = linspace(a, b, precision)
    dx = float(b - a) / (int(precision)-1)
    left_point_values = func(x[:-1])
    right_point_values = func(x[1:])
    return dx * sum(left_point_values + right_point_values) / 2.


def anti_derivative(func, x, precision=100.):
    """ Simple numerical evaluation of the anti-dericative of a function func
    at various points x. Only used for the Bonus Bonus question.
    """
    result = []
    for b in x:
        result.append(integrator(func, 0, b, precision=precision))
    return array(result)

if __name__ == "__main__":
    # Sample code to use this integrator: let's integrate the constant function
    # f(x) = 1.
    def cst(x):
        return ones(len(x))

    print(integrator(cst, 0, 10))
