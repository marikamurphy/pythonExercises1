"""
Tests for Test Driven Development Example
-----------------------------------------

Develop your tests for the ``fancy_math`` module in this file.  See that module
for the full exercise instructions.

See: :ref:`test_fancy_math_solution`.

"""

from numpy import Inf
from nose.tools import assert_almost_equal, assert_equal

from fancy_math import slope

def test_slope_inf():
    '''See if infinite slope is caught'''
    pt1 = [0,0]
    pt2 = [0,1]
    s = slope(pt1, pt2)
    assert_almost_equal(s, Inf)
    
    pt1 = [0,1]
    pt2 = [0,0]
    s = slope(pt1, pt2)
    assert_almost_equal(s, -Inf)
    
def test_slope_int():  
    '''Test for int'''  
    pt1 = [0,0]
    pt2 = [2,1]
    s = slope(pt1, pt2)
    assert_almost_equal(s, 0.5)

def test_slope_float():
    '''Test for float'''    
    pt1 = [0.0,0.0]
    pt2 = [1.0,1.0]
    s = slope(pt1, pt2)
    assert_almost_equal(s, 1)
    
def test_slope_identical():
    '''Test for identical points'''
    pt1 = [0.0,0.0]
    pt2 = [0.0,0.0]
    s = slope(pt1, pt2)
    assert s == 'und'
    
