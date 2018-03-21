"""
Particle Table
--------------

Use a TableEditor to create a table that displays a list of
Particle instances.

0. The Particle class is defined for you below.

1. Define a ParticleList class, derived from HasTraits, that
   holds a list (trait type `List`) of Particles in a trait
   called `particles`.  Create a view of this class that displays
   the list using a TableEditor.  The table should have three
   columns: mass, velocity and momentum.

   For similar examples, see:

    * Demos/traits_examples/table_example/table_2.py
    * The example in "Standard Editors / TableEditor demo" in
      the TraitsUI demo program.

2. Add another column to the table that displays the
   relativistic momentum::

     p = m * v / sqrt(1 - v**2 / c**2)

  where `c` is the speed of light.  Assume we are using
  metric units and `c` is given in meters per second.

  To use `c` and `sqrt` in the expression, you will have
  to use the 'globals' keyword, which lets you provide
  additional names in a dictionary.  E.g.::

      ExpressionColumn(label="Rel. momentum",
                       expression="...fill this in...",
                       globals=dict(sqrt=sqrt, c=c))

  By using `globals`, you will be able to use the names
  `c` and `sqrt` in your expression.

  `c` may be imported from scipy::

    from scipy.constants import c

  and `sqrt` from math::

    from math import sqrt

  These imports are provided for you in the code below.

See :ref:`particle-table-solution`.
"""

from traits.api import HasTraits, Float, Property, List
from traitsui.api import View, Item, Group
from traitsui.menu import OKCancelButtons

from traitsui.api import TableEditor
from traitsui.table_column import ObjectColumn, ExpressionColumn

from math import sqrt
from scipy.constants import c


class Particle(HasTraits):

    # The mass of the particle.
    mass = Float

    # The velocity of the particle.
    velocity = Float

    # The energy of the particle.
    energy = Property(Float, depends_on=['mass', 'velocity'])

    # The momentum of the particle.
    momentum = Property(Float, depends_on=['mass', 'velocity'])

    def _get_energy(self):
        return 0.5 * self.mass * self.velocity ** 2

    def _get_momentum(self):
        return self.mass * self.velocity


class ParticleList(HasTraits):
    
    particles = List
    
    view = View(
                Group(
                    Item('particles', editor=TableEditor(columns=[
                        ObjectColumn(name='mass'),
                        ObjectColumn(name='velocity'),
                        ObjectColumn(name='momentum'),
                        ExpressionColumn(label='Rel. momentum',
                        expression="object.momentum / \
                        sqrt(1 - object.velocity**2 / c**2)",
                        globals=dict(sqrt=sqrt, c=c))  

                    ]
                    )),
                    
                    ),
                    resizable=True,
                    buttons=OKCancelButtons
                
                )
    
    

if __name__ == "__main__":
    # Make a list of Particles for testing.
    p1 = Particle(mass=0.1, velocity=10.0)
    p2 = Particle(mass=1.2, velocity=1.25e5)
    p3 = Particle(mass=0.25, velocity=2.0e8)
    p4 = Particle(mass=10.0, velocity=8.4e6)
    plist = ParticleList(particles=[p1, p2, p3, p4])
    plist.configure_traits()
