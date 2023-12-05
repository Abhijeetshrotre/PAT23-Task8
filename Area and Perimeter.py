class Rectangle:
    def __init__(self, dimensions_list):
        # Initialize the length and width of the rectangle from the given list
        self.length = dimensions_list[0]
        self.width = dimensions_list[1]

    def calculate_area(self):
        """
        area = length * width
        """
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        """
        Perimeter = 2 * (length + width)
        """
        perimeter = 2 * (self.length + self.width)
        return perimeter

# Example usage with a given list
dimensions_list = [5, 10]

# Create an instance of the Rectangle class
rectangle_instance = Rectangle(dimensions_list)

# Calculate and print the area and perimeter
area = rectangle_instance.calculate_area()
perimeter = rectangle_instance.calculate_perimeter()

print(f"For a rectangle with length {dimensions_list[0]} and width {dimensions_list[1]}:")
print(f"  Area: {area}")
print(f"  Perimeter: {perimeter}")