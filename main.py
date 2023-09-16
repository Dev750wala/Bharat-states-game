"""Turtle graphics"""
import turtle
import pandas as pd
from mapping import Mapping, EndGame

screen = turtle.Screen()
IMAGE = "blank_states_img.gif"
screen.title("Bharat states game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

guessed_number = 0
guesssed_states = []

data = pd.read_csv("states_coords.csv")
states = list(data.state)

while guessed_number is not 27:

    user_input = screen.textinput(title=f"{guessed_number}/{len(data)} States Correct", prompt="What's other states name?").title()
    # user_input.lower()
    print(user_input)

    if user_input == "Exit":
        break
    elif user_input in states and user_input not in guesssed_states:
        guesssed_states.append(user_input)
        temp = data[data["state"] == user_input]
        state_name = Mapping(user_input, temp.x, temp.y)
        state_name.write_name()
        guessed_number += 1
    if guessed_number is 27:
        end_game = EndGame()
        break

if guessed_number is not 27:
    not_guessed = []

    for state in data["state"]:
        if state not in guesssed_states:
            not_guessed.append(state)

    state_dict = {
        "State": not_guessed
    }

    frame = pd.DataFrame(state_dict)
    frame.to_csv("not_guessed_states.csv")

screen.exitonclick()
