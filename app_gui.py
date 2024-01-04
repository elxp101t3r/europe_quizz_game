from turtle import Turtle, Screen
import pandas as pd

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
        self.data = pd.read_csv('eu_countries.csv')
        
        self.count_correct = 0
        self.answer = self.screen.textinput(title=f"{self.count_correct}/36 Correct Countries", prompt="What's another country name?")
        self.data_l = list(self.data['country'])
        for self.country in self.data_l:
            if self.country == self.answer:
                self.count_correct += 1
                
                print(self.count_correct)
            
            
            
        