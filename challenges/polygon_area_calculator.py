class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __repr__(self):
        arg_list = [f"{key}={val}" for key, val in vars(self).items()]
        args = ", ".join(arg_list)
        return f"{self.__class__.__name__}({args})"
        
    def set_width(self, new_width):
        self.width = new_width
        
    def set_height(self, new_height):
        self.height = new_height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        row_of_stars = self.width * "*"
        return "\n".join([row_of_stars for _ in range(self.height)]) + "\n"
    
    def get_amount_inside(self, other):
        if other.width > self.width or other.height > self.height:
            return 0
        num_along = self.width // other.width
        num_down = self.height // other.height
        return num_along * num_down
        

class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)
        
    def __repr__(self):
        return f"{self.__class__.__name__}(side={self.width})"
    
    def set_side(self, side):
        self.width = side
        self.height = side
        
    def set_width(self, new_side):
        self.width = new_side
        self.height = new_side
        
    def set_height(self, new_side):
        self.height = new_side
        self.width = new_side

# rect = Rectangle(width=49, height=3)
# print(rect.get_picture())
# print(rect)

square = Square(side=3)
print(square)
square.set_height(4)
print(square)
print(square.get_picture())