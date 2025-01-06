class Rectangle:
    # Dunder init method is actually a method that runs once the object has been created
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if value < 0:
            print("width must be +ve")
        else:
            self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if value < 0:
            print("height must be +ve")
        else:
            self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self._width, self._height)

    def __eq__(self, other):
        # check other is intance of Rectangle
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return False

r1=Rectangle(10,20)
print(r1.width)
print(r1.height)

r1.width=800
r1.height=-600
print(r1.area())
print(r1)