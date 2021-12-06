from turtle import Turtle, Screen
import random

race_active = False
screen = Screen()
screen.setup(width=500, height=400)
turtle_bet = screen.textinput(title="silahkan pilih!", prompt="PROGRAM GAME SEDERHANA (KURA-KURA RACING)\nmenurutmu kura-kura mana yang akan menang? silahkan pilih warnanya\n(merah = red, biru = blue, orange = orange, kuning = yellow, hijau = green atau ungu = purple): ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = (-100, -60, -20, 20, 60, 100)
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=(y_positions[turtle_index]))
    all_turtles.append(new_turtle)

if turtle_bet:
    race_active = True

while race_active:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_active = False
            winning_colour = turtle.pencolor()
            if winning_colour == turtle_bet:
                print(f"selamat, kamu menang! >> {winning_colour} turtle is a winner.")
            else:
                print(f"yaaah.... kamu kalah.. >> {winning_colour} turtle is a winner!.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
