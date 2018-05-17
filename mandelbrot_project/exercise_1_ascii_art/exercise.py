"""
Mandelbrot set ASCII art
------------------------

At the start of this file we define a function to compute the escape times at
a given coordinate (x, y) in the Mandelbrot set. For the moment, you can
use it as a black box that can be called as

    >>> time = mandelbrot_escape(-1, 0.5)

You can read the docstring to have more details about the arguments of the
function:

    >>> help(mandelbrot_escape)


1. Compute the escape times at these (x, y) coordinates:
   coords = [(-1, 0.5), (-1, 0), (0.5, -0.3), (0.5, 0.3)]

   The expected result is [4, -1, 5, 5]

2. Build a list-of-lists of the Mandelbrot set escape times on a 21x21 grid
   of coordinates between  x = -2 ... 1  and y = -1.5 ... 1.5 .

   The result is going to look similar to this:
   [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 2, 2, ...],
    ...
    [0, 0, 0, 0, 0, 1, ...]]

3. Use the escape times to create an ASCII-art representation of the
   Mandelbrot set, e.g.

...............::::::::::::::::::::::::::::::::::::::::::::::::
............:::::::::::::::::::::::::::::::::::::::::::::::::::
.........:::::::::ooooooooooooooooooooooooooo::::::::::::::::::
......::::::ooooooooooooooooooOOOOOO###HHHOOOoooooo::::::::::::
......:::oooooooooooooooOOOOOOOOO000######000OOOoooooo:::::::::
...:::oooooooooooooooOOOOOO000HHHXXX      XXX000OOOoooooo::::::
...:::ooooooooooooOOO000000XXX               ######oooooo::::::
...oooooooooOOOHHH000HHHXXX                     XXXOOOoooooo:::
...oooOOOOOO000############                     ###OOOoooooo:::
...OOOOOO000######                              ###OOOoooooo:::
...                                             XXXOOOoooooo:::
...OOOOOO000######                              ###OOOoooooo:::
...oooOOOOOO000############                     ###OOOoooooo:::
...oooooooooOOOHHH000HHHXXX                     XXXOOOoooooo:::
...:::ooooooooooooOOO000000XXX               ######oooooo::::::
...:::oooooooooooooooOOOOOO000HHHXXX      XXX000OOOoooooo::::::
......:::oooooooooooooooOOOOOOOOO000######000OOOoooooo:::::::::
......::::::ooooooooooooooooooOOOOOO###HHHOOOoooooo::::::::::::
.........:::::::::ooooooooooooooooooooooooooo::::::::::::::::::
............:::::::::::::::::::::::::::::::::::::::::::::::::::
...............::::::::::::::::::::::::::::::::::::::::::::::::

"""

def mandelbrot_escape(x, y, n=100):
    """Mandelbrot set escape time algorithm for a given c = x + i*y coordinate.

    Return the number of iterations necessary to escape abouve a fixed threshold
    (4.0) by repeatedly applying the formula:

    z_0 = 0
    z_n = z_{n-1} ^ 2 + c

    If the formula did not escape after `n` iterations, return -1 .

    Parameters
    ----------
    x, y -- float
        Real and imaginary part of the complex number z.

    n -- integer
        Maximum number of iterations.
    """

    z_x = 0
    z_y = 0

    for i in range(n):
        z_x, z_y = z_x**2 - z_y**2 + x,  2*z_x*z_y + y

        # If we are diverging, return the number of iterations.
        if z_x**2 + z_y**2 >= 4.0:
            break
    else:
        i = -1

    return i
    
    

def test_mand(coords):
    
    values = [mandelbrot_escape(x,y) for (x,y) in coords]
    return values    
    

def find_mand_coords(size=21, x_init=-2, x_fin=1, y_init=-1.5, y_fin=1.5):


    mand_values = []
    x_step = float(x_fin-x_init) / (size-1)
    y_step = float(y_fin-y_init) / (size-1)
    

    for y in range(0,size):
        temp = []
        y_coord = y_init + y * y_step
    
        for x in range(0, size):
            x_coord = x_init + x * x_step
            temp.append(mandelbrot_escape(x_coord, y_coord))
    
        mand_values.append(temp)
        
        
    return mand_values 

def create_ascii(coords):
    
    equivalents = {-1:'.',0:')',1:'!',2:'@',
                    3:'#',4:'$',5:'%',6:'^',7:'&',
                    8:'*',9:'(',10:';',11:':',12:'/',
                    13:'\\',14:'|',16:'<',18:'>',27:'+'}
    
    string_ascii = ""
    for arr in coords:
        for val in arr:
            string_ascii+=equivalents[val]   
        string_ascii+='\n'
        
    return string_ascii
            
                              
coords = [(-1, 0.5), (-1, 0), (0.5, -0.3), (0.5, 0.3)]         
print(test_mand(coords))

coords = find_mand_coords()
print(create_ascii(coords))