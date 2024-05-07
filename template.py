"""
Fractal Animation Template

This template provides a starting point for creating and animating fractals using Manim.

Usage:
1. Define the Fractal object, set new_points_func and base_coords_complex attributes.
2. Choose the number of generations to draw and build the fractal.
3. Define a scene class for animating the fractal.

To customize the animation, modify the provided functions and parameters as needed.

Author: [Your Name]
Date: [Date]
"""

from fractal_lib.fractal import *

# Initialize a Fractal object
fractal = Fractal()

# Define a function for generating new points
def new_points(p1, p2):
    # Choose any value between 0 and 1 for the scalars
    scalar1 = 1/3
    scalar2 = 2/3
    
    # Calculate new points creatively using p1, p2, and complex numbers
    # As long as n1, n2, and n3 are in terms of p1 and p2, you should be able to make interesting fractals (feel free to modify / get rid of scalars and see examples for inspiration)
    n1 = p1 + (p2 - p1) * scalar1 
    n2 = p1 + (p2 - p1) / 2 + (((p2 - p1) * 3**(1/2)) / 3 / 2) * 1j # You can modify this line to your liking, as long as n2 is in terms of p1, p2, and includes a complex component it will be fun
    n3 = p1 + (p2 - p1) * scalar2 
    
    return n1, n2, n3

# Set the new_points_func attribute of the fractal object to the defined function
fractal.new_points_func = new_points

# Set the initial base coordinates for the fractal 
initial_points = [complex(0,0), complex(1,0)]
fractal.base_coords_complex = initial_points

# Choose the number of generations you want to draw (more than 8 gets slow)
n = 6

# Build the fractal with the specified number of generations
fractal.build(n)

# Define a scene class for animating the fractal
class curve(MovingCameraScene):
    def construct(self):
        """
        This method constructs the animation scene.
        Don't need to modify this unless you want to customize the animation further.
        Once it's customized to your liking, run the following command in the terminal:
        manim -pqh template.py curve
        """
        # Play the animation for each object in the fractal
        for i in range(len(fractal.mobjects)):
            self.play(Create(fractal.mobjects[i], rate_func=linear),
                      self.camera.frame.animate(rate_func=linear).scale(0.85),
                      run_time=0.7 - 0.025 * i)
        self.wait()

# End of template