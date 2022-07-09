class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height)
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
        return self.diagonal


    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            self.pict = ""
            for i in range(self.height):
                self.pict = self.pict + f"{'*' * self.width}\n"
            return self.pict
        else:
            return "Too big for picture."

    def get_amount_inside(self, another):
        multiple_with = (self.width // another.width)
        multiple_height = (self.height // another.height)
        times = multiple_with * multiple_height
        return times


    def __repr__(self):
        string = "Rectangle(width={}".format(self.width) + ", height={}".format(self.height) + ")"
        return string
        print(type(string))


class Square(Rectangle):

    def __init__(self,side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def set_side(self, side):
        self.side = side
        self.width = self.side
        self.height = self.side

    def __repr__(self):
        string = "Square(side={}".format(self.width) + ')'
        return string
        print(type(string))


dreptunghi = Rectangle(15, 10)

d_a = dreptunghi.get_area()
print(d_a)

d_p = dreptunghi.get_perimeter()
print(d_p)

d_diag = dreptunghi.get_diagonal
print(d_diag)

d_pict = dreptunghi.get_picture()
print(d_pict)


#patrat = Rectangle("dreptunghi")
#patrat.set_height(10)
#patrat.set_width(5)
patrat = Square(4)
#patrat.set_side(5)

d_a = patrat.get_area()
print(d_a)
d_p = patrat.get_perimeter()
print(d_p)
d_pict = patrat.get_picture()
print(d_pict)


an = dreptunghi.get_amount_inside(patrat)
print(an)

print(dreptunghi)
print(patrat)