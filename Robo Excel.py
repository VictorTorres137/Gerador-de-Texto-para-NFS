# from pandas import *
import pandas as pd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import FileChooserIconView, FileChooser


class Prog(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def mudatexto(self):
        self.ids.bt2.text="12343434"
        self.ids.lb1.text = "12343434"
        self.ids.fl2.add_widget(FileChooser(pos_hint={"x": .0, "y": .0}, size_hint=[1, .8]))


    # def procura(self):
    #
    #     filename = filedialog.askopenfilename(initialdir="/",
    #                                           title="Select a File",
    #                                           filetypes=(("Excel",
    #                                                       ".xlsx"),
    #                                                      ("all files",
    #                                                       ".")))
    #     return filename


class Tela(App):
    def build(self):
        return Prog()

Tela().run()


#
#
# arquivo = pd.read_excel("Eco Urbis-Container-0256-22-Sul.xlsx")
#
# print(arquivo)

