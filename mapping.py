from turtle import Turtle


class Mapping(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.x = x
        self.y = y
        self.goto(int(self.x), int(self.y))
        self.state = state

    def write_name(self):
        self.write(arg=self.state, move=False, align="center", font=('Arial', 8, 'normal'))


class EndGame(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.write(arg="Congratulations! You answered all the states name correct.🥳", move=False, align="center",
                   font=('Arial', 20, 'normal'))