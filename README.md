# Fractal Generation and Visualization

This project is a Python implementation of fractal generation and visualization using the Manim library. It includes functions to generate fractals iteratively and visualize them using Manim's animation capabilities.
The fractal.py file in fractal_lib contains the fractal class which is used to generate the examples.

## Features

- **Fractal Generation:** The project includes functions to generate fractals iteratively, allowing users to specify the number of generations and the function to create new points.
  
- **Visualization:** Fractals are visualized using Manim, enabling users to create animations that illustrate the iterative construction process.

## Usage

1. **Installation:**
   - Clone the repository to your local machine.
   - Install the required dependencies (Manim)

2. **Generating Fractals: Quick Start**
   - Define the function to create new points in the `new_points` function. (see template.py and examples).
   - Create an instance of the `Fractal` class and set the `new_points_func` attribute to the desired function.
   - Call the `build` method with the desired number of generations to generate the fractal.
   - Use command `manim -pqh file_name.py scene_name` (see template.py for example)

3. **Visualization:**
   - Use the generated Manim objects in your Manim scene to visualize the fractal animation (see template.py).

## Example

```python
from fractal_lib import Fractal
from draw import new_points

# Create an instance of the Fractal class
fractal = Fractal()

# Set the function to create new points
fractal.new_points_func = new_points

# Build the fractal
fractal.build(5)

# Use the generated Manim objects in your Manim scene

```

## Demos
[<img src="https://img.youtube.com/vi/Nv-0p6jQK80/hqdefault.jpg" width="600" height="300"
/>](https://www.youtube.com/watch?v=Nv-0p6jQK80)
To generate these demos from the code, run the following commands in the project directory:

`manim -pqh koch_example.py curve`

`manim -pqh right_angles_example.py curve`

`manim -pqh shifted_example.py curve`