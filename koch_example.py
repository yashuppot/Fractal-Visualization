
from fractal_lib.fractal import *

fractal = Fractal()

def new_points(p1, p2):
    scalar1 = 1/3
    scalar2 = 2/3
    
    n1 = p1 + (p2 - p1) * scalar1 
    n2 = p1 + (p2 - p1) / 2 + (((p2 - p1) * 3**(1/2)) / 3 / 2) * 1j # You can modify this line to your liking, as long as n2 is in terms of p1, p2, and includes a complex component it will be fun
    n3 = p1 + (p2 - p1) * scalar2 
    
    return n1, n2, n3

fractal.new_points_func = new_points
initial_points = [complex(0-1.5,0-1.5*3**(0.5)/2), complex(1.5-1.5,1.5*3**(0.5)-1.5*3**(0.5)/2), complex(3-1.5,0-1.5*3**(0.5)/2), complex(0-1.5,0-1.5*3**(0.5)/2)] #triangle centered at origin
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