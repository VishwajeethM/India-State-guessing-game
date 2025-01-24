from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(100, 270)
        self.states_guessed = 0
        self.union_guessed = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"India's states: {self.states_guessed}/28 Union territories: {self.union_guessed}/8",
                   align="center", font=("Arial", 16, "normal"))

    def state_inc(self):
        self.states_guessed += 1
        self.update()

    def union_inc(self):
        self.union_guessed += 1
        self.update()

    def give_up(self):
        self.clear()
        self.write(f"States not guessed: {28 - self.states_guessed} "
                   f"Union territories not guessed: {8 - self.union_guessed}",
                   align="center", font=("Arial", 16, "normal"))

    def show_congratulation(self):
        # Create a new turtle for the message

        # Set up the message
        self.goto(0, 0)
        self.color("green")
        self.write("Congratulations! You Won!", align="center", font=("Arial", 24, "bold"))
