
from fractal_lib.fractal import *

fractal = Fractal()

def new_points(p1, p2):
    scalar1 = 0.5
    scalar2 = 0.75
    
    n1 = p1 + (p2 - p1) * scalar1 
    n2 = p1 + (p2 - p1) / 2 + (((p2 - p1) * 2**(1/2)) / 3 / 2) * 1j 
    n3 = n2 + n2 * 1j
    
    return n1, n2, n3

fractal.new_points_func = new_points
initial_points = [complex(0,0), complex(1,0)] 
fractal.base_coords_complex = initial_points

n = 6

fractal.build(n)

class curve(MovingCameraScene):
    def construct(self):
        for i in range(len(fractal.mobjects)):
            self.play(Create(fractal.mobjects[i], rate_func=linear),
                      self.camera.frame.animate(rate_func=linear).scale(0.85),
                      run_time=0.7 - 0.025 * i)
        self.wait()