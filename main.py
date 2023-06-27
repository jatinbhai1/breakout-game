import turtle
import random


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
    if pong.xcor()>-550:
        pong.goto(pong.xcor()-15, pong.ycor())
def move_right():
    if pong.xcor() < 550:
        pong.goto(pong.xcor() + 15, pong.ycor())

#herea adding a pong
root.tracer(0)
pong = turtle.Turtle(shape='square')
pong.color('white')
pong.penup()
pong.shapesize(1,13)
pong.goto(1, -453)
root.update()
root.tracer(1)

root.onkeypress(fun=move_left, key='Left')
root.onkeypress(fun=move_right, key='Right')

key_pressed = root.listen()


root.mainloop()
