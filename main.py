import turtle
IMAGE = 'europe.gif'

screen = turtle.Screen()
screen.setup(width=600, height=480)
screen.title('Europe Quiz Game')
screen.addshape(IMAGE)
turtle.shape(IMAGE)

answer = screen.textinput(title=f'Guess the Europen country', prompt="What's another country name?")

