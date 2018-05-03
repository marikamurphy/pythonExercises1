import numpy as np



def mandelbrot_escape(x_grid, y_grid, n=100):
    
    
    times = np.full(x_grid.shape, -1, dtype=int)
    z_x = 0
    z_y = 0

    for i in range(n):
        z_x, z_y = z_x**2 - z_y**2 + x_grid,  2*z_x*z_y + y_grid

        # If we are diverging, return the number of iterations.
        div_mask = z_x**2 + z_y**2 >= 4.0
        times[div_mask & (times==-1)] = i
        
        z_x[np.where(times!=-1)] = 0
        z_y[np.where(times!=-1)] = 0 #why does this shorten runtimes?
    

   
    return times
        
    
    
    

def find_mand_coords(size=21, x_init=-2, x_fin=1, y_init=-1.5, y_fin=1.5):#grid


    
    x_coords = np.linspace(x_init,x_fin,size)
    y_coords = np.linspace(y_init,y_fin,size)
    x_grid, y_grid = np.meshgrid(x_coords,y_coords)
      
        
    return mandelbrot_escape(x_grid, y_grid) 
  

