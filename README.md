# Fractals

Exploring computational generation and rendering fractals using Python


---

This is primarily an educational tool, mostly for myself, to explore the generation of fractals in Python.

There's a lot of stuff left to do.

## KNOWN ISSUES
- [ ] Changing the number of iterations changes the overall colour of the main bulb. In principle, nothing should change. But that is indeed very curious.
- [ ] Algorithm breaks for non-square aspect ratios. Isn't a big enough deal right now for me to work on it.

## TODO

- [x] Change backend from Matplotlib to Pillow to directly draw onto a Canvas
- [ ] Improve coloring algorithms
	- [x] Write HSV colormaps
	- [ ] Write LCH colormaps
- [ ] Use symmetry across y-axis to cut down time in half
- [ ] Employ multithreading, especially because this problem apparently is _embarrassingly parallel_.
- [ ] Write out similar code for other kinds of fractal sets, like Julia, for instance
- [ ] Create an interface that can control the resolution and type of fractal
- [ ] Create an animation zoom automatedly that zooms into a specific point and renders things on the fly (might have to learn how the perturbative techniques work)