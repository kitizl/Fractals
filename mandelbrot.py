import numpy as np
import matplotlib.pyplot as plt
import time

class Pixel:
    """
    A class to manage Pixel properties
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

def rescale(number, width, min_val, max_val):
    """
    A function to rescale values based on resolutions
    """
    return (max_val-min_val)*number/width + min_val

# here, we are only implementing the optimized-ish algorithm

def optimized_escape_time_alogrithm(x_width, y_width):
	xs = np.arange(0,x_width)
	ys = np.arange(0,y_width)

	screen = np.asarray([[Pixel(x, y, 0) for x in xs] for y in ys]).flatten()
	for pixel in screen:
		x0 = rescale(pixel.x, x_width, -2.00, 0.47)
		y0 = rescale(pixel.y, y_width, -1.12, 1.12)
		x = 0
		y = 0
		iteration = 0
		max_iter = 1000

		x2 = 0
		y2 = 0
		while ((x2 + y2 <= 4) and (iteration < max_iter)):
			y = 2 * x * y + y0
			x = x2 - y2 + x0
			x2 = x * x
			y2 = y * y
			iteration += 1
		pixel.color = iteration
	
	pixel_color = [pixel.color for pixel in screen]
	reshaped_screen = np.reshape(pixel_color, (x_width,y_width))

	plt.figure(figsize=(x_width//20, y_width//20))
	plt.title(f"{x_width}x{y_width}")
	plt.imshow(reshaped_screen, interpolation="none")
	plt.show()
  
start = time.time_ns()

optimized_escape_time_alogrithm(200,200)

end = time.time_ns()

print(f"Optimized time : {(end-start)/(1e9):1.3e} s")