class Rectangle:
    # Dunder init method is actually a method that runs once the object has been created
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self,w):
        if w<=0:
            raise ValueError("width must be greater than 0")
        else:
            self._width = w

    def get_height(self):
        return self._height

    def set_height(self,h):
        if h<=0:
            raise ValueError("height must be greater than 0")
        else:
            self._height = h

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

    def get_width(self):
        return self._width




r1=Rectangle(10,20)
r1.set_width(10)
r1.set_height(20)
print(r1.area())
print(r1.perimeter())
print(str(r1))
r2=Rectangle(10,20)
print(r1==r2)

print(r1==100)
print(r1 < r2)

# RAISE ERROR
# r2.set_width(-10)
# r2.set_height(-20)