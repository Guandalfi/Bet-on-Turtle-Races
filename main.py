from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Which turtle will win", "chose the turtle color")


colors = ["blue", "red", "yellow", "orange", "green", "purple"]
initial_pos = [-100, -70, -40, -10, 20, 50]
turtles = []


for turtle_index in range(0,6):
    tr = Turtle(shape="turtle")
    tr.penup()
    tr.color(colors[turtle_index])
    tr.goto(x=-230, y=initial_pos[turtle_index])
    turtles.append(tr)
    tr.color()


winner = False
while not winner:
        turtle_1 = turtles[0].forward(random.randint(2,10))
        turtle_2 = turtles[1].forward(random.randint(2,10))
        turtle_3 = turtles[2].forward(random.randint(2,10))
        turtle_4 = turtles[3].forward(random.randint(2,10))
        turtle_5 = turtles[4].forward(random.randint(2,10))
        turtle_6 = turtles[5].forward(random.randint(2,10))
        for i in turtles:
            if i.xcor() >= 240:
                print(f"{i.xcor()},turtle color: {i}")
                winner_turtle = i
                winner = True


print(f"The winner was turtle: {winner_turtle.color()[0]}")
if user_bet == winner_turtle.color()[0]:
    print("You win the bet")
else:
    print("You did not win the bet")


screen.exitonclick()