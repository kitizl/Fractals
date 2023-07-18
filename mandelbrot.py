import numpy as np
from PIL import Image
import time

MAX_ITER = 10000
WIDTH = 100
HEIGHT = WIDTH


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
		MAX_ITER = 1000

		x2 = 0
		y2 = 0
		while ((x2 + y2 <= 4) and (iteration < MAX_ITER)):
			y = 2 * x * y + y0
			x = x2 - y2 + x0
			x2 = x * x
			y2 = y * y
			iteration += 1
		pixel.color = iteration
	
	pixel_color = [pixel.color for pixel in screen]
	reshaped_screen = np.reshape(pixel_color, (x_width,y_width))

	return reshaped_screen
  
def convert2HSV(arr):
    """
    Takes in an array and maps the iteration values to some HSV
    value, as determined by the exponential mapping formula.
    
	Takes in an array, returns an array
    """
    iter_vals_flattened = arr.flatten()
    hue_vals = ((iter_vals_flattened/MAX_ITER * 255)**1.5)%255
    sat_vals = np.ones(hue_vals.shape)*255
    val_vals = iter_vals_flattened/MAX_ITER * 255
    hsv_vals = np.dstack((hue_vals, sat_vals, val_vals)).reshape((*arr.shape, 3)).astype()
    return hsv_vals


start = time.time_ns()

raw_array = optimized_escape_time_alogrithm(WIDTH, HEIGHT)
print(raw_array.shape)

end = time.time_ns()

print(f"Generating the fractal took {(end-start)*1e-9:1.3e}s")

start = time.time_ns()
hsv_array = convert2HSV(raw_array)
end = time.time_ns()

print(f"Converting values to HSV took {(end-start)*1e-9:1.3e}s")
# produce the HSV fractal

start = time.time_ns()

hsv_img = Image.fromarray(hsv_array, mode="HSV")

# display the image
hsv_img.show()
end = time.time_ns()

print(f"Converting array to image and displaying took {(end-start)*1e-9:1.3e}s")