import math

class Circle:
    def __init__(self, radius_list):
        # Private member variable for pi
        self._pi = 3.141

        # Public  variable for radii
        self.radius_list = radius_list

    def print_radii(self):
        """
        Print the list of radii.
        """
        print("Radii:")
        for radius in self.radius_list:
            print(f" - {radius}")

    def calculate_diameters(self):
        """
        Calculate diameters for each radius in the list.Formula: diameter = 2 * radius
        """
        diameters = [2 * r for r in self.radius_list]
        return diameters

    def calculate_circumference_to_diameter_ratio(self):
        """
        Calculate the ratio of circumference to diameter for each radius in the list.
        Formula: ratio = 2 * pi * radius / (2 * radius)
        """
        ratios = [2 * self._pi * r / (2 * r) for r in self.radius_list]
        return ratios

# Example
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_list)

circle_instance.print_radii()
diameters = circle_instance.calculate_diameters()
ratios = circle_instance.calculate_circumference_to_diameter_ratio()

for i, radius in enumerate(radius_list):
    print(f"For circle with radius {radius}:")
    print(f"  Diameter: {diameters[i]}")
    print(f"  Circumference-to-Diameter Ratio: {ratios[i]:.2f}")
    print()