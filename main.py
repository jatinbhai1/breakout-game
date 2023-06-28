import turtle
import random

game_over = False
height = 1000
width = 1400
root = turtle.Screen()
root.title('Breakout game')
root.bgcolor('black')
root.setup(width=width, height=height)
colors = ['blue', 'green', 'yellow', 'red', 'white', 'gray', 'navy', 'skyblue']
block_turtle_list = []
def add_turtle_block():
    root.tracer(0)
    for k in range(8):

        for i in range(width//105):

            block = turtle.Turtle('square')

            block.width(width=40)
            block.shapesize(2, 5)
            block.color(random.choice(colors))
            block.penup()
            block_turtle_list.append(block)
            block.goto(-640+(i*105),400-k*50)
    root.update()
    root.tracer(1)
add_turtle_block()

def move_left():
    if pong.xcor()>-580:
        pong.goto(pong.xcor()-25, pong.ycor())
def move_right():
    if pong.xcor() < 580:
        pong.goto(pong.xcor() + 25, pong.ycor())

#herea adding a pong
root.tracer(0)
pong = turtle.Turtle(shape='square')
pong.color('white')
pong.penup()
pong.shapesize(1,8)
pong.goto(1, -453)
root.update()
root.tracer(1)



ball = turtle.Turtle('circle')
root.tracer(0)
ball.color('white')
ball.penup()
hide_tur = 0
def bounce():
        ball.setheading(ball.heading()+60)
ball.goto(x=0, y=-301)
root.update()
ball.setheading(70)
to_do = 0
while not game_over:


    ball.forward(3)
    if ball.xcor()>670 or ball.xcor()<-670 or ball.ycor()>485 or ball.ycor()<-490:
        ball.right(70)

    if ball.distance(pong)<60:
        bounce()





    for block in block_turtle_list:
        if ball.distance(block)<50:
            block.hideturtle()
            hide_tur +=1
    if ball.ycor()<-480:
        tim = turtle.Turtle()
        tim.color('white')
        tim.goto(0,0)
        tim.penup()
        tim.write('You lose',font=("Verdana",
                                    15, "normal"))

        break

    if hide_tur==len(block_turtle_list):
        tim = turtle.Turtle()
        tim.color('white')
        tim.penup()
        tim.write('You win',font=("Verdana",
                                    15, "normal"))
        break


    root.onkeypress(fun=move_left, key='Left')
    root.onkeypress(fun=move_right, key='Right')

    key_pressed = root.listen()
    root.update()

root.mainloop()
