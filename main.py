import turtle
import pandas as pd
IMAGE = 'europe.gif'

screen = turtle.Screen()
screen.setup(width=600, height=480)
screen.title('Europe Quiz Game')
screen.addshape(IMAGE)
turtle.shape(IMAGE)

count_correct = 0

while True:
    answer = screen.textinput(title=f'{count_correct}/36 Guess the Europen country', prompt="What's another country name?")

    if answer is not None:
        title_case = answer.title()

        df = pd.read_csv('eu_countries.csv')

        for x in df['country']:
            if title_case == x:
                count_correct += 1
                