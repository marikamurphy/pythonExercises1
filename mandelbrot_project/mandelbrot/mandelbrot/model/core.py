def mandelbrot_escape(x, y, n=100):
    

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