import math class Circle:def
__init__ (self, radius):
self.radius = radius def area (self):


return math.pi * self.radius ** 2 class Cylinder (Circle):


def __init__ (self, radius, height):


super ().__init__ (radius) self.height = height def area (self):





circle_area = super ().area ()lateral_area = 2 * math.pi * self.radius * self.height return 2 * circle_area + lateral_area def volume (self):




return math.pi * self.radius ** 2 * self.height
  radius_circle = 5
  circle_instance = Circle (radius_circle)
print (f "Circle Area: {circle_instance.area()}")
radius_cylinder = 3
height_cylinder = 8
cylinder_instance = Cylinder (radius_cylinder, height_cylinder)
print (f "Cylinder Area: {cylinder_instance.area()}") print (f "Cylinder Volume: {cylinder_instance.volume()}")
