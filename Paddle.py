import turtle 

class Paddle:
    def __init__(self, player_no, name = 'Player'):
        # Create a paddle
        self.paddle = turtle.Turtle()
        
        self.name = name 
        self.score = 0 
        
        self.paddle.speed(0)

        self.paddle.shape('square')
        self.paddle.color('black')
        self.paddle.shapesize(stretch_wid = 6, stretch_len = 2)
        self.paddle.penup()
        
        if player_no == 2:
            self.paddle.goto(400,0)
        else: 
            self.paddle.goto(-400,0)
        pass 
    
    def goUp(self):
        val = self.paddle.ycor() + 20
        self.paddle.sety(val) 
        
    def goDown(self):
        val = self.paddle.ycor() - 20
        self.paddle.sety(val) 
    
    def getX(self):
        return self.paddle.xcor()

    def getY(self):
        return self.paddle.ycor() 

    def earnPoint(self):
        self.score += 1

    def position(self,x = None, y = None):
        if x is not None:
            self.paddle.setx(x)
        if y is not None:
            self.paddle.sety(y)
        return 
