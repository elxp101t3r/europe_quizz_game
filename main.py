import turtle
import pandas as pd
import csv
IMAGE = 'europe.gif'

screen = turtle.Screen()
screen.setup(width=600, height=480)
screen.title('Europe Quiz Game')
screen.addshape(IMAGE)
turtle.shape(IMAGE)
t = turtle.Turtle()
count_correct = 0

while True:
    answer = screen.textinput(title=f'{count_correct}/36 Guess the Europen country', prompt="What's another country name?")

    if answer is not None:
        title_case = answer.title()

        df = pd.read_csv('eu_countries.csv')

        for i, x in df.iterrows():
            if title_case == x['country']:
                count_correct += 1
                t.penup()
                t.hideturtle()
                t.goto(x['cordinate_x'], x['cordinate_y'])
                t.write(title_case)
                             