import turtle
import time
import random

# Setup screen
win = turtle.Screen()
win.title("Simple Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
direction = "stop"

# Food
food = turtle.Turtle()
food.speed(10)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Body segments
segments = []

# Movement functions
def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

def move():
    global direction
    if direction == "up":
        head.sety(head.ycor() + 20)
    if direction == "down":
        head.sety(head.ycor() - 20)
    if direction == "left":
        head.setx(head.xcor() - 20)
    if direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# Main game loop
while True:
    win.update()

    # Check for collision with border
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

    # Check for collision with food
    if head.distance(food) < 20:
        # Move food to random location
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

    # Move the segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()
    time.sleep(0.1)
