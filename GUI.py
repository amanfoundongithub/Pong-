import turtle 
from Paddle import Paddle
from Ball import Ball
from ScoreBoard import Scoreboard

screen = turtle.Screen()

screen.title('PONG GAME')
screen.bgcolor('yellow')
screen.setup(width = 1000, height = 600)

paddle_1 = Paddle(player_no = 1)
paddle_2 = Paddle(player_no = 2)

scores   = Scoreboard() 

ball = Ball() 

screen.listen()
screen.onkeypress(paddle_2.goUp,    "Up")
screen.onkeypress(paddle_2.goDown,"Down")
screen.onkeypress(paddle_1.goUp,     "w")
screen.onkeypress(paddle_1.goDown,   "s")

while True: 
    screen.update()
    ball.move()
    
    if ball.getY() > 280 or ball.getY() < -280:
        ball.changeDirection(along_y = True) 
    
        if ball.getY() > 0:
            ball.position(y = 280)
        else:
            ball.position(y = -280)
    
    if ball.getX() > 500 or ball.getX() < -500:
        if ball.getX() > 0:
            paddle_1.earnPoint()
        else: 
            paddle_2.earnPoint()
        
        scores.updateScore(paddle_1, paddle_2)
        ball.position(x = 0,y = 0)
        ball.changeDirection(along_x = True) 
        
        
    # Bat ball collision
    if (ball.getX() > 360 and ball.getY() < 370) and abs(ball.getY() - paddle_2.getY()) <= 40:
        ball.position(x = 360)
        ball.changeDirection(along_x = True) 
    
    if (ball.getX() <  -360 and ball.getY() > -370) and abs(ball.getY() - paddle_1.getY()) <= 40:
        ball.position(x = -360)
        ball.changeDirection(along_x = True) 
            
    
            
        

screen.mainloop()