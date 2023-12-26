import turtle 


class Scoreboard:
    def __init__(self):
        
        self.board = turtle.Turtle()
        
        self.board.speed(0)
        self.board.color('blue')
        self.board.penup()
        self.board.hideturtle() 
        self.board.goto(0,260)
        self.board.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))
    
    def updateScore(self, paddle_1, paddle_2):
        self.board.clear()

        score = "Left_player : {}    Right_player: {}".format(paddle_1.score, paddle_2.score)
        
        self.board.write(score, align = 'center', font = ('Courier',24, 'normal'))
    




















'''
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
'''