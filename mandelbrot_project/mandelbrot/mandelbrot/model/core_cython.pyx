""" Core math functions to compute escape times for the Mandelbrot set. """

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

def mandelbrot_grid(x_bounds, y_bounds, size=40):
    """ Return escape times at a grid of coordinates.

    Escape times are computed on a grid of size given by the `size` argument.
    x coordinates start at x_bounds[0] and end at x_bounds[1].
    y coordinates start at y_bounds[0] and end at y_bounds[1].

    """
    
    escape_times = []

    x0, x1 = x_bounds
    y0, y1 = y_bounds

    width = x1 - x0
    height = y1 - y0

    for i in range(size+1):
        row = []
        for j in range(size+1):
            x = j / float(size) * width + x0
            y = i / float(size) * height + y0
            t = mandelbrot_escape(x, y, 100)
            row.append(t)

        escape_times.append(row)

    return escape_times
