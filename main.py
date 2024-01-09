import turtle
import pandas as pd

IMAGE = 'europe.gif'

screen = turtle.Screen()
screen.setup(width=600, height=480)
screen.title('Europe Quiz Game')
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pd.read_csv('eu_countries.csv')
all_countries = data.country.to_list()

guessed_countries = []

while len(guessed_countries) < 36:
    answer = screen.textinput(title=f'{len(guessed_countries)}/36 Countries | Guess the country', prompt='Whats the next country?').title()

    if answer in all_countries:
        guessed_countries.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer]
        t.goto(int(country_data.cordinate_x), int(country_data.cordinate_y))
        t.write(country_data.country.item(), align='center')

screen.exitonclick()