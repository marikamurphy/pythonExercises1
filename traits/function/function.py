"""
Trait Function
--------------

Traits-based class for calculating a function.

1. Write a Traits-based class that calculates the following signal::

       y = a*exp(-b*x) + c

   Make *a*, *b*, and *c* floating point traits with default
   values of 2.0, 0.76, 1.0. The *x* variable should be an array
   trait with the default value [0, 0.5, 1, 1.5, ..., 5.0].
   The *y* value should be a property trait that updates any time
   *a*, *b*, *c* or *x* changes.

   Once your class is defined, create an instance of the object and
   print its *y* value.

2. Define a function `printer(value)` that prints an array, and set
   it to be an external trait listener for the trait *y* on the
   instance created in 1, so *y*'s value it printed whenever it
   changes.

3. Create a UI that displays *a*, *b*, and *c* as text boxes.

4. Create a UI that displays *a*, *b*, and *c* as sliders,
   and *x* and *y* as read-only arrays.  Use an ArrayEditor for the
   display of the arrays, and set the 'width' keyword of the
   ArrayEditor to a value large enough for the values in the array.

See: :ref:`trait-function-solution`.
"""

from traitsui.api import View, Item
from traits.api import HasTraits, Float, Property, Array
from numpy import linspace, exp, set_printoptions, get_printoptions
from traitsui.api import RangeEditor, ArrayEditor

# 1. Create class that updates y whenever a, b, c or x change.

class Exponential(HasTraits):

    # Amplitude.
    a = Float(2.0)

    # Fill in your code here.
    #exponential constant
    b = Float(0.76)
    
    #offset
    c = Float(1.0)
    
    x = Array
    
    y = Property( depends_on=['a','b','c','x'] )
    
    
    def _get_y(self):
        return self.a * exp(-self.b * self.x) + self.c
    
    def _x_default(self):
        return linspace(0.0, 5.0, 6)
        
    


func = Exponential()
print(func.y)

'''
Now we have an exponential object 'func' that we can modify:
    give it a unique printer method
    give it a unique UI
the class serves to show what should be universal to this kind of object,
we get our own addons
'''

# 2. Define a function `printer(value)` that prints an array, and set
#    it to be an external trait listener for the trait *y*.
def printer(value):
    opt = get_printoptions()
    set_printoptions(precision=2)
    print("new value: ", value)
    set_printoptions(**opt)
    
    
func.on_trait_change(printer, name='y')
'''
Above sets the printer method to being an external trait listener for y
'''
    

# 3. Create a UI that displays a, b, and c as text boxes.

# Set up a view.
simple_view = View('a','b','c')

# Use it for your traits.
func.edit_traits(view=simple_view)


# 4. Create a UI that displays a, b, and c as sliders.
slide_view = View(
                    Item('a', editor=RangeEditor(low=0.0, high=15.0)),
                    Item('b', editor=RangeEditor(low=0.0, high=15.0)),
                    Item('c', editor=RangeEditor(low=0.0, high=15.0)),
                    Item('x', editor=ArrayEditor()),
                    Item('y', editor=ArrayEditor(), style='readonly'),
                    resizable=True
                    
                    )
func.edit_traits(view=slide_view)
