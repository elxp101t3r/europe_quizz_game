'''
Needs resize of the bgpic, csv with coordinates in x y format and names of all the countries
'''

import turtle

IMAGE = 'europe.gif'

screen = turtle.Screen()
screen.title('Europe Countries Quiz')

screen.addshape(IMAGE)

turtle.shape(IMAGE)

screen.exitonclick()