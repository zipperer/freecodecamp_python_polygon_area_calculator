class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return ((2 * self.width) + (2 * self.height))

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** .5

    def get_picture(self):
        if ((self.width > 50) or (self.height > 50)):
            return 'Too big for picture.'
        else:
            line = '*' * self.width
            lines = [line for i in range(self.height)]
            shape = '\n'.join(lines)
            shape = shape + '\n'
            return shape

    def get_amount_inside(self, shape_object): # shape_object is Rectangle or Square
        shape_object_width = shape_object.width
        shape_object_height = shape_object.height
        amount_can_stack_inside_vertically = int(self.height / shape_object_height) # int() to round down
        amount_can_lay_inside_horizontally = int(self.width / shape_object_width)
        amount_inside = amount_can_stack_inside_vertically * amount_can_lay_inside_horizontally
        return amount_inside

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):

    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def __str__(self):
        return f'Square(side={self.width})'
