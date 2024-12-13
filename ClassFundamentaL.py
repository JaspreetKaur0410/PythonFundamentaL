class Rectangle:
    # Dunder init method is actually a method that runs once the object has been created
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

r1=Rectangle(10,20)
print(r1.width)
print(r1.height)
print(r1.area())
print(r1.perimeter())