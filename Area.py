import math
pi = math.pi

def circle(radius): # pie * r^2
    return pi*(radius**2)
def cube(side):
    return 6*side**2
def cylinder(radius,height):
    return 2*pi*radius + 2*pi*height
def sphere(radius):
    return 2*pi*(radius**2)

print(sphere(16))