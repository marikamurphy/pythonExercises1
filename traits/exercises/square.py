from traits.api import HasTraits, CFloat, Property
from traitsui.api import View, Item, VGroup, HGroup, OKCancelButtons
from rectangle import Rectangle

class Square(Rectangle):
    
    
    
    square_view = View(
                    
                    Item('width', label = 'Side length'),
                    Item('area', style='readonly'),
                    buttons=OKCancelButtons
    
    )
    
    def _get_area(self):
        return self.width**2
        
square = Square()
square.edit_traits('view')
square.edit_traits('square_view')


