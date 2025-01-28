from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, go_to):
        super().__init__() # We inherit from the parent class
        self.shape("square")
        self.color("orange")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.paddle_speed = 20
        self.speed(10)
        self.goto(go_to)
        self.moving_left = False # The base movement state of our paddle
        self.moving_right = False # The base movement state of our paddle


    def move_left(self):
        """The function that determines the move to the left. While True will keep moving left"""
        self.moving_left = True
        self.move_paddle()


    def move_right(self):
        """The function that determines the move to the right. While True will keep moving right"""
        self.moving_right = True
        self.move_paddle()


    def stop_left(self):
        """Only here to stop our padle dead in it's tracks"""
        self.moving_left = False


    def stop_right(self):
        """Only here to stop our paddle dead in it's tracks"""
        self.moving_right = False


    def move_paddle(self):
        """The moving function, that incorporates the coordinate variables and conditionals"""
        if self.moving_left:
            if self.xcor() >= -310:
                x = self.xcor()
                self.setx(x - self.paddle_speed)
        if self.moving_right:
            if self.xcor() <= 310:
                x = self.xcor()
                self.setx(x + self.paddle_speed)
