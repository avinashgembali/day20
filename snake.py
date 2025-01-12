from turtle import Turtle

STARTING_POSITION = [(-40, 0), (-20, 0), (0, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.goto(position)
            self.segments.append(t)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)