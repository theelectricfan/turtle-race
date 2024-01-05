import random
import turtle

screen = turtle.Screen()
screen.setup(height=400, width=500)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle_list = []

for n in range(len(colors)):
    turtle_list.append(turtle.Turtle(shape="turtle"))
    turtle_list[n].color(colors[n])
    turtle_list[n].penup()
    turtle_list[n].goto(x=-230, y=-125 + 50 * n)

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a colour {colors}: ")
race_over = False
while not race_over:
    for n in range(len(turtle_list)):
        if turtle_list[n].xcor() > 230:
            race_over = True
            winner_color = turtle_list[n].fillcolor()
            print(f"{winner_color.capitalize()} turtle has won the race!")
            if user_bet == winner_color:
                print("Congratulations! You've won.")
            else:
                print("You have lost!")
            break
        turtle_list[n].forward(random.randint(1, 10))
