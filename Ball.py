import turtle


class Ball: 
    def __init__(self):
        
        self.ball = turtle.Turtle()
        
        self.ball.shape('circle')
        self.ball.color('red')
        
        self.ball.speed(40) 
        self.ball.penup()
        self.ball.goto(0,0)
        
        self.dx = 5
        self.dy = -5
        
    def move(self):
        self.ball.sety(self.ball.ycor() + self.dy)
        self.ball.setx(self.ball.xcor() + self.dx) 
    
    def getX(self):
        return self.ball.xcor()

    def getY(self):
        return self.ball.ycor() 
    
    def position(self,x = None,y = None):
        if x is not None:
            self.ball.setx(x)
        if y is not None:
            self.ball.sety(y)
        return 

    def changeDirection(self, along_x = False, along_y = False):
        if along_x:
            self.dx = - self.dx 
        
        if along_y:
            self.dy = - self.dy 
        