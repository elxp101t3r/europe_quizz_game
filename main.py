import turtle
import time
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

    if answer == 'Exit':
        a_c = set(all_countries)
        g_c = set(guessed_countries)
        countries_to_learn = a_c.difference(g_c)
        df = pd.DataFrame(countries_to_learn, columns=['Missing Countries to Learn'])
        df.to_csv('countries_to_learn.csv')
        check_point = True
        break
    if answer in all_countries:
        guessed_countries.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer]
        t.goto(int(country_data.cordinate_x), int(country_data.cordinate_y))
        t.write(country_data.country.item(), align='center')
if len(guessed_countries) == 36 or check_point == True:
    screen.clear()
    screen.setup(width=600, height=550)
    message = "Congratulations! You have completed the quiz."
    turtle.hideturtle()
    turtle.penup()
    turtle.write(message, move=False, align="center", font=('Comic', 15, 'normal'))
    time.sleep(1.5)
    screen.clear()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-60,-250)
    turtle.write(df)
    screen.exitonclick()