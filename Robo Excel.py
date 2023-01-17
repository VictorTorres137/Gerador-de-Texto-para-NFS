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

# class Filechooser(FloatLayout):
#     def select(self, *args):
#         try: self.label.text = args[1][0]
#         except: pass


class Prog(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def mudatexto(self):

        self.caminho=FileChooserIconView(pos_hint={"x": .0, "y": .0}, size_hint=[1, .7])
        self.btok = Button(text="OK", pos_hint={"x": .35, "y": .8}, size_hint=[.3, .1], on_release=lambda a='' : self.seleciona_arquivo())


        self.ids.fl2.add_widget(self.btok)
        self.ids.fl2.add_widget(self.caminho)

        # return self.caminho

    def seleciona_arquivo(self):
        print(self.caminho.selection[0])
        str_caminho_do_arquivo = self.caminho.selection
        print(self.caminho.selection)
        arquivo = pd.read_excel(str_caminho_do_arquivo[0])

        print(arquivo.iloc[20,0])

        self.ids.fl2.remove_widget(self.btok)
        self.ids.fl2.remove_widget(self.caminho)


class Tela(App):
    def build(self):
        return Prog()

Tela().run()


#
#
# arquivo = pd.read_excel("Eco Urbis-Container-0256-22-Sul.xlsx")
#
# print(arquivo)

