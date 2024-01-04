from turtle import Turtle, Screen
IMAGE = 'europe.gif'


class Window_app(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.title('Europe Countries Quiz')
        self.screen.addshape(IMAGE)
        self.shape(IMAGE)
        self.question_box = QuestionBox()
        

class QuestionBox(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.answer = self.screen.textinput(title="Guess the Country", prompt="What's another country name?")