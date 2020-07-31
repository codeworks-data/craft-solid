# Interface segregation principle


class Shape:
    def draw_circle(self):
        raise NotImplemented

    def draw_square(self):
        raise NotImplemented


class Circle(Shape):
    def draw_circle(self):
        print("o")

    def draw_square(self):
        pass


class Square(Shape):
    def draw_circle(self):
        pass

    def draw_square(self):
        print("[]")
