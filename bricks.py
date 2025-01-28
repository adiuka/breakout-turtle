from turtle import Turtle
import random




# A chat_GBT generated color list inspired by the rainbow :D
RAINBOW = [
    "red", "tomato", "orange", "gold", "yellow", "green", "lime", "cyan", "blue", "royalblue", "indigo", "purple", "violet", "orchid"        
]

class Brick(Turtle):
    """The Class Defining the Brick Object using the Turtle Module"""
    def __init__(self, X, Y):
        super().__init__() # Inherit from the parent class
        self.penup() # We raise the pen to avoid drawing
        self.shape('square') # Set the shape to resemble a block to break
        self.shapesize(stretch_wid=1.5, stretch_len=3) # We set the size of the brick to be destroyed
        self.color(random.choice(RAINBOW)) # Picks a random color from our rainbow
        self.goto(x=X, y=Y) # Goes to the coordinates provided

        # Reading online I saw that I need to detect the coordinates of each and every side of the brick for propper detection. 
        # My reasoning is that they are 15 wid and 30 len in each direction
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15


class Bricks:
    """The class defining the list of lanes of Brick Objects"""
    def __init__(self):
        self.y_start = 0 # Bottom
        self.y_end = 240 # Top
        self.bricks = [] # Empty list for Brick Objects
        self.create_rows() # Call the function to create the rows.


    def create_row(self, Y):
        """Creates a row for the coordinate range, with specific coordinate significance to leave a space between a Brick and screen Margins"""
        for i in range(-375, 390, 62): # Creates the range in which to place a lane of bricks. Note our brick size is 80 so I added a bit of space in between
            brick = Brick(i, Y) # Creates a brick object at the given coordinates, where the turtle object will goto()
            self.bricks.append(brick) # Creates and appends brick into a list of bricks

    
    def create_rows(self):
        """Drops down the rows on the Y axis """
        for i in range(self.y_start, self.y_end, 32): # Takes in our brick thickness into consideration here when bulding the various lanes
            self.create_row(i) # Creates a lane using the previous function 

