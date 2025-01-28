from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__() # Inherit from the parent class
        self.shape('circle')
        self.color('white')
        self.penup()
        self.y_move_dist = 10
        self.x_move_dist = 10
        self.ball_reset() # Makes sure the ball starts in the original position

    
    def move(self):
        """The function that defines the ball's movement. Based on the self.move_dist class variable"""
        new_x = self.xcor() + self.x_move_dist
        new_y = self.ycor() + self.y_move_dist
        self.goto(new_x, new_y)


    def bounce(self, x_bounce, y_bounce):
        """The bounce function, inspired by a StackedOverflow post, that used True and False statements to change directions"""
        if x_bounce:
            self.x_move_dist *= -1 # Multiplying by - 1 turns the coordinate inclination positive or negative

        if y_bounce:
            self.y_move_dist *= -1


    def ball_reset(self):
        """Resets the ball position"""
        self.goto(x=0, y=-220) # The original position
        self.y_move_dist = 10 # Sets the position to pisitive so it always goes the same way



