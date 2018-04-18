"""
Software craftsmanship
======================
1. Open the compute_integral module and look at the integrator function. This
function takes a function and 2 boundaries and returns the integral of that
function between the boundaries. Test if this funcion gives correct results on
simple functions you know the integral of. Find cases where it doesn't.

2. We want to improve this function. Design and then write some unit tests to
make sure the funcion keeps giving correct results where it already does and
write some tests that the function is currently failing. These tests will guide
us while improving it. The goal is to write enough unit tests such that it is
impossible to break the function without breaking one of our tests and
therefore knowing it. That usually requires multiple tests, covering all
aspects of the function (different types of functions, all possible ways to
call the function, ...).

To run all your tests, you can run
$ nosetests -v
from the command line.

Bonus:
~~~~~~
3. Make the function pass all tests by fixing the errors.

Bonus Bonus:
~~~~~~~~~~~~
4. We used the integrator to build a function that computes the anti-derivative
of any function. Write one more unit test to make sure that anti_derivative
provides the correct result for the cosine function, that is a function that
is equal to the sin function over [0, 2pi]. You will need to look into
numpy.testing for the needed assertion function for this question.

See :ref:`test_integral_solution`.
"""
from compute_integral import integrator, anti_derivative
from numpy import ones, sin, pi, cos, linspace
import unittest

class IntegratorTester(unittest.TestCase):

    def test_integrator_cst(self):
        """ Test integration of the constant function 1
        """
        def cst_func(x):
            return ones(x.shape)

        # Your test here
        self.assertAlmostEqual(integrator(cst_func, 0, 10), 10)

    def test_integrator_x(self):
        """ Test integration of the function x
        """
        # Your test here
        def func(x):
            return x
        
        self.assertAlmostEqual(integrator(func, 0, 10), 50)

    def test_integrator_x_high_res(self):
        """ Test integration of the function x with a higher precision
        """
        # Your test here
        def func(x):
            return x
            
        self.assertAlmostEqual(integrator(func, 0, 10, 1000), 50)

    def one_more_test_integrator(self):
        """ What else should we test?
        """
        # Your test here

    def test_anti_derivative(self):
        """ Bonus Bonus: Test computing the anti-derivative of the cosine
        function and compare it to the sin function over the [0, 2pi] interval.
        """
        # Your test here
        def func_cos(x):
            return cos(x)
        
        self.assertAlmostEqual(integrator(func_cos, 0, 2*pi), (sin(2*pi)- sin(0)))

if __name__ == "__main__":
    unittest.main()
