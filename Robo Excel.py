# from pandas import *
import pandas as pd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


class Tarefa(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class Tela(App):
    def build(self):

        return Tarefa()

Tela().run()


#
#
# arquivo = pd.read_excel("Eco Urbis-Container-0256-22-Sul.xlsx")
#
# print(arquivo)

