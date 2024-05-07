"""
Fractal Generation with Manim Visualization

This script defines a Fractal class that generates a fractal based on a given function to create new points and visualizes it using Manim. 
The fractal is built iteratively up to a specified number of generations, and each generation is represented as a set of Manim VMobjects.

Author: Yash Uppot

Date: 2023-06-06

Dependencies: Manim

Usage:
    - Create an instance of the Fractal class.
    - Set the new_points_func attribute to the function that creates new points (see template file and examples)
    - Call the build method with the desired number of generations to build the fractal.
    - The build_mobjects method is automatically called within the build method to create Manim objects.
"""

from manim import *

class Fractal:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.new_points_func = None  # Function to create new points from 2 given points
        self.base_coords_complex = [complex(0,0), complex(0,1)]; # Base coordinates of generation 0
        self.base_coords = []  # Coordinates of each generation
        self.mobjects = []  # Manim objects representing each generation
    
    def build_next_gen(self):
        """
        Generate points for the next generation of the fractal.

        Returns:
            list of complex: Next generation of points.
        """
        nextgen = []
        for i in range(len(self.base_coords_complex) - 1):
            nextgen.append(self.base_coords_complex[i])
            n1, n2, n3 = self.new_points_func(self.base_coords_complex[i], self.base_coords_complex[i + 1])
            nextgen.extend([n1, n2, n3])
        n1, n2, n3 = new_points(self.base_coords_complex[-1], self.base_coords_complex[0])
        nextgen.extend([self.base_coords_complex[-1], n1, n2, n3, self.base_coords_complex[0]])
        return nextgen
    
    def build(self, n):
        """
        Build the fractal up to the specified number of generations.

        Parameters:
            n (int): Number of generations to build.
        """
        for i in range(n):
            self.base_coords_complex = self.build_next_gen()
            self.base_coords.append([])
            for j in self.base_coords_complex:
                re = j.real
                im = j.imag
                self.base_coords[i].append([re, im, 0])
        self.build_mobjects()

    def build_mobjects(self):
        """
        Create Manim objects for each generation of the fractal.
        """
        i = 1
        for coords in self.base_coords:
            l = VMobject(stroke_width=2/(i))
            l.set_points_as_corners(coords).set_color([BLUE, GREEN, RED])
            self.mobjects.append(l)
            i += 1

        


    
