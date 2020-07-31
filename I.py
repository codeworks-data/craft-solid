# Interface segregation principle


class Shape:
    def draw_shape(self):
        raise NotImplemented


class Circle(Shape):
    def draw_shape(self):
        print("o")


class Square(Shape):
    def draw_shape(self):
        print("[]")
