import turtle
import pandas
from scoreboard import Scoreboard


# setting up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

# Turtle graphics
T = turtle.Turtle()
T.hideturtle()
T.penup()

# showing scoreboard
score_board = Scoreboard()
score_board.update()

# Getting the map image
image = "resized_india_map.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("India States Game")


# Reading csv data
state_data = pandas.read_csv("Coordinates/states_coordinates.csv")
union_data = pandas.read_csv("Coordinates/union_coordinates.csv")


all_states = state_data.state.to_list()
all_unions = union_data.union.to_list()
guessed_states = []
guessed_union = []
score = 0

while score != 36:
    screen.update()
    # Getting user input
    if score == 0:
        answer = screen.textinput(title="Quiz", prompt="Enter INDIA's state/union name.").title()
    else:
        answer = screen.textinput(title=f"{score}/36 guessed", prompt="What's another state name?").title()

    # Exiting from quiz
    if answer == "Exit":
        missing_states = []
        missing_union = []
        for state in state_data.state:
            if state not in guessed_states:
                missing_states.append(state)
        for union in union_data.union:
            if union not in guessed_union:
                missing_union.append(union)
        # new_data = pandas.DataFrame(missing_states)
        # new_data.to_csv("states_to_learn.csv")
        print(f"States that you didn't guess : \n{missing_states}")
        print(f"Union tert that you didn't guess : \n{missing_union}")
        break

    if answer in all_states:
        score_board.state_inc()

        guessed_states.append(answer)
        row = state_data[state_data.state == answer]
        cord = (row.x.item(), row.y.item())

        T.goto(tuple(cord))

        T.write(arg=answer, align="center", font=("Arial", 8, "normal"))

        score += 1

    if answer in all_unions:
        score_board.union_inc()

        guessed_union.append(answer)
        row = union_data[union_data.union == answer]
        cord = (row.x.item(), row.y.item())

        T.goto(tuple(cord))

        T.write(arg=answer, align="center", font=("Arial", 8, "normal"))

        score += 1

    if answer == "Give Up":
        T.goto(200, 200)
        T.write(f"Score: {score}/36", align="center", font=("Arial", 12, "bold"))
        score_board.give_up()
        T.color("red")
        for state in all_states:
            if state not in guessed_states:

                row = state_data[state_data.state == state]
                cord = (row.x.item(), row.y.item())

                T.goto(tuple(cord))

                T.write(arg=state, align="center", font=("Arial", 10, "normal"))

        for union in all_unions:
            if union not in guessed_union:

                row = union_data[union_data.union == union]
                cord = (row.x.item(), row.y.item())

                T.goto(tuple(cord))

                T.write(arg=union, align="center", font=("Arial", 10, "normal"))

        break


if score == 36:
    score_board.show_congratulation()


screen.exitonclick()
