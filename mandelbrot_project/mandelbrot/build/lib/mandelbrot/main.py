from __future__ import print_function
from mandelbrot.model.numpy_core import find_mand_coords
from mandelbrot.ui.ascii import create_ascii

def main():
    coords = find_mand_coords()
    print(create_ascii(coords))
    
if __name__ == '__main__':
    print('--------- WELCOME TO THE MANDELBROT PLOTTING APPLICATION! ---------\n')
    main()