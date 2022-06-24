from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles_list = []
n = 0
is_race_on = False
for turtles in colors:
    turtle = Turtle(shape="turtle")
    turtle.speed(1)
    turtle.color(turtles)
    turtle.penup()
    turtle.goto(x=-230, y=-100 + n)
    n += 40
    turtles_list.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for new_turtle in turtles_list:
        if new_turtle.xcor() > 220:
            is_race_on = False
            if new_turtle.pencolor() == user_bet:
                print(f"You win! The winner is {new_turtle.pencolor()}")
            else:
                print(f"You lose! The winner is {new_turtle.pencolor()}")

        new_turtle.forward(random.randint(1, 11))


screen.exitonclick()
