import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_plastic():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    plastic = f.generate()
    # Add noise to the fractal shape to make it look more like plastic
    noise = np.random.normal(0, 0.05, plastic.shape)
    plastic = plastic + noise
    plastic = np.clip(plastic, 0, 1)
    # Apply a plastic-like color map to the fractal shape
    plastic = plt.cm.Greens(plastic)
    # Return the fractal plastic
    return plastic

# Generate 10 fractal plastic images
for i in range(10):
    plastic = generate_fractal_plastic()
    plt.imsave("fractal_plastic_{}.png".format(i), plastic)
