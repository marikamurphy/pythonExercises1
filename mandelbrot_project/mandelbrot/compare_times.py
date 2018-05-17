from __future__ import print_function
from timeit import default_timer as time
from mandelbrot.model.core import find_mand_coords as mg_python
from mandelbrot.model.core_numpy import find_mand_coords as mg_numpy


start_time = time()
escape_time = mg_python()
print("Runtime pure python"+str(escape_time-start_time))

start_time = time()
escape_time = mg_numpy()
print("Runtime with numpy"+str(escape_time-start_time))
