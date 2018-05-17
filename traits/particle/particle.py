"""
Trait Particle
--------------

Define a Traits-based class for a Particle.

1. Define a Particle class derived from HasTraits. A Particle
   should have a :attr:`mass` and a :attr:`velocity` that are both
   floating point values.  It should also have two read-only
   Property traits, :attr:`energy` and :attr:`momentum`, given
   by::

       energy = 0.5 * mass * velocity **2
       momentum = mass * velocity

   After defining the class, create an instance of it and set/get
   some its traits to test its behavior.

2. Create a UI that groups the mass and velocity side-by-side at
   the top of a dialog with the energy and momentum below.

See :ref:`trait-particle-solution`.
"""

from __future__ import print_function
from traits.api import HasTraits, Float, Property
from traitsui.api import View, VGroup, HGroup, Item
from traitsui.menu import OKCancelButtons


class Particle(HasTraits):
    
    mass = Float
    
    velocity = Float
    
    momentum = Property(depends_on=['mass', 'velocity'])
    
    energy = Property(depends_on=['mass', 'velocity'])
    
    view = View(
                VGroup(
                        HGroup(
                                Item('mass'),
                                Item('velocity')
                                ),
                                
                        HGroup(
                                Item('energy', style='readonly', width=100),
                                Item('momentum', style='readonly', width=100)
                            ),
                                
                        ),
                buttons=OKCancelButtons

                )
    
    
    def _get_momentum(self):
        return self.mass * self.velocity
        
    def _get_energy(self):
        return 0.5 * self.mass * self.velocity**2
        
    


if __name__ == "__main__":
    p = Particle(mass=2, velocity=1.5)
    print("energy is", p.energy)
    p.configure_traits()
    print("energy is", p.energy)
