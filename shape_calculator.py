class Rectangle:
  width = 0
  height = 0
  def __init__(self, widthr, heightr):
    self.width = widthr
    self.height = heightr
    return

  def set_width(self,widthr):
    self.width = widthr
    return

  def set_height(self, heightr):
    self.height = heightr
    return

  def get_area(self):
    arear = self.width*self.height
    return arear

  def get_perimeter(self):
    perimeter = (2 * self.width + 2 * self.height)
    return perimeter

  def get_diagonal(self):
    diagr = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagr

  def get_picture(self):
    pic = ''
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    for h in range(self.height):
      for w in range(self.width):
        pic += '*'
      pic += '\n'
    return pic

  def get_amount_inside(self,shape):
    fittimes = int(self.get_area()/shape.get_area())
    return fittimes

  def __str__(self):
    
    return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'



class Square(Rectangle):
  side = 0
  def __init__(self, sides):
    self.width = sides
    self.height = sides
    self.side = sides
    return

  def set_side(self, sides):
    self.width = sides
    self.height = sides
    self.side = sides

    return

  def set_width(self,widthr):
    self.width = widthr
    self.height = widthr
    self.side = widthr
    return

  def set_height(self, heightr):
    self.height = heightr
    self.width = heightr
    self.side = heightr
    return
  
  def __str__(self):
    
    return 'Square(side='+ str(self.side) +')'