from app_gui import Window_app
import pandas as pd

w = Window_app()

df = pd.read_csv('eu_countries.csv')
print(df)
df.to_excel('data.xlsx')