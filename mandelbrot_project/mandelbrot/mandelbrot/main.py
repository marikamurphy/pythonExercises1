from __future__ import print_function
from mandelbrot.model.numpy_core import find_mand_coords
from mandelbrot.model.core_cython import mandelbrot_grid
from mandelbrot.ui.ascii import create_ascii
from mandelbrot.ui.simple_plot import plot_mandelbrot 

def main():
    x_init = -2
    x_fin = 1
    y_init = -1.5
    y_fin = 1.5
    coords = find_mand_coords()
    print(create_ascii(coords))
    plot_mandelbrot(coords, x_init, x_fin, y_init, y_fin)
    
if __name__ == '__main__':
    print('------- WELCOME TO THE MANDELBROT PLOTTING APPLICATION! -------\n')
    main()