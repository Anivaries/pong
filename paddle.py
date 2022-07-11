from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, set_pos) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.up()
        self.goto(set_pos)

    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)