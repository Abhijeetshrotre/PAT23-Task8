import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def print_radii(self):
        print("Radii:")
        for radius in self.radius_list:
            print(f" - {radius}")

    def calculate_areas(self):
        areas = [math.pi * r**2 for r in self.radius_list]
        return areas

    def calculate_circumferences(self):
        circumferences = [2 * math.pi * r for r in self.radius_list]
        return circumferences

# Example
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_list)

circle_instance.print_radii()
areas = circle_instance.calculate_areas()
circumferences = circle_instance.calculate_circumferences()

for i, radius in enumerate(radius_list):
    print(f"For circle with radius {radius}:")
    print(f"  Area: {areas[i]:.2f}")
    print(f"  Circumference: {circumferences[i]:.2f}")
    print()
