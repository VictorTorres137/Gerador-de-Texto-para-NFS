# from pandas import *
import pandas as pd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Gui=Builder.load_file('menu.kv')


class AwesomeApp(App):
    def build(self):
        return Gui

if __name__ == "__main__":
    AwesomeApp().run()


#
#
# arquivo = pd.read_excel("Eco Urbis-Container-0256-22-Sul.xlsx")
#
# print(arquivo)

