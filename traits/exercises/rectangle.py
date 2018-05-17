from traits.api import HasTraits, CFloat, Property
from traitsui.api import View, Item, VGroup, HGroup, OKCancelButtons

class Rectangle(HasTraits):
    
    width = CFloat(1.0)
    
    height = CFloat(2.0)
    
    area = Property(depends_on=['width','height'])
    
    view = View(
                VGroup(
                    HGroup(
                        Item('width', label='W'),
                        Item('height', label='H')
                    ),
                    Item('area', style='readonly'),
                ),
                
                buttons=OKCancelButtons

        )
    
    def _get_area(self):
        
        return self.width * self.height


        

rect = Rectangle(width=2.0, height="3.0")

rect.edit_traits()


