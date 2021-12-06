import turtle

trtl = turtle.Turtle()   
screen=turtle.Screen()    
screen.setup(420,320)    
trtl.pencolor('black')   
trtl.pensize(5)    
trtl.shape('turtle')   
n=0   
while n<15:  
    n=n+1   
    trtl.penup()   
    trtl.setpos(0,-n*20)   
    trtl.pendown()   
    trtl.circle(20*n)   

