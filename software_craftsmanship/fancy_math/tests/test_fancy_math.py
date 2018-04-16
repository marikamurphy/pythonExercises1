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

def test_slope_und():
    '''See if undefined slope is caught'''
    assert slope([0,0],[0,0]) == 'und'
    
def test_slope_int():  
    '''Test for int'''  
    assert slope([0,0],[1,1]) == 1

def test_slope_float():
    '''Test for float'''    
    assert slope([0.0,0.0],[1.0,1.0]) == 1.0
    
