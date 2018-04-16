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

def test_slope_xxx():
    assert slope([1,2],[2,3]) == 1.0
