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
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    n_lines = int(self.height)
    n_asterisk = int(self.width)
    if ((n_lines > 50) or (n_asterisk > 50)):
      return "Too big for picture."
    string = ""
    for i in range(n_lines):
      for j in range(n_asterisk):
        string += "*"
      string += "\n"
    return string

  def get_amount_inside(self, shape):
    width_fit = int(self.width / shape.width)
    height_fit = int(self.height / shape.height)

    return (width_fit * height_fit)

  def __str__(self):
    string = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return string

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    string = "Square(side=" + str(self.width) + ")"
    return string

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.height = height
    self.width = height