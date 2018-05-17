import matplotlib.pyplot as plt

def plot_mandelbrot(coords, x_init, x_fin, y_init, y_fin):
    plt.imshow(coords, extent=(x_init, x_fin, y_init, y_fin))
    plt.show()
    
