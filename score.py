from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.create_middleline()
        self.create_scoreboard(x,y)


    def create_middleline(self):
        middleline = Turtle('classic')
        middleline.penup()
        middleline.goto(300,0)
        self.score =0
        for num in range(600):
            middleline.forward(20)
            middleline.penup()
            middleline.forward(20)
            middleline.pendown()

    def create_scoreboard(self,x,y):
        text = Turtle()

        text.goto(x, y)
        text.write(arg=f'Score_A={self.score}', align='center', font=('Arial', 18, 'normal'))


    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score_A={self.score}', align='center', font=('Arial', 18, 'normal'))
