class Rectangle:
    pass
    
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

      class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width  

        class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

        class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def circumference(self):
        return 2 * (self.length + self.width)

        class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def circumference(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

        class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def circumference(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle, {self.length} cm long, and {self.width} cm wide"

        length = float(input("Enter length: "))

while length == 0:
    print("Input cannot be 0!")
    length = float(input("Enter length: "))

    width = float(input("Enter width: "))

while width == 0:
    print("Input cannot be 0!")
    width = float(input("Enter width: "))

    rectangle = Rectangle(length, width)

print(rectangle)
print("Circumference:", rectangle.circumference(), "cm")
print("Area:", rectangle.area(), "cm²")