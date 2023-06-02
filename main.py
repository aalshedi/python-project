import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(10)  # Set the speed of the turtle

# Set initial position and color
t.penup()
t.goto(-200, 0)
t.pendown()
t.color("white")

# Draw the angular design
for _ in range(36):  # Repeat the pattern 36 times
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)  # Rotate the turtle slightly for the next iteration

# Hide the turtle
t.hideturtle()

# Exit the turtle screen on click
turtle.done()
