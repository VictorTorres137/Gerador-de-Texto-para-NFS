# from pandas import *
import pandas as pd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import *


# from openpyxl
procura_arquivo_parent = aviso_selecione_arquivo_parent= "None"

class Info():
    def __init__(self, num_orc, num_nf, cabc, desct, vencm, *serv):
        self.num_orc = num_orc
        self.num_nf = num_nf
        self.cabc = cabc
        self.desct = desct
        self.vencm = vencm
        self.serv = serv


class Prog(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.bt1 = Button(text='Procure o Arquivo', size_hint=[.3, .1], pos_hint={"x": .35, "y": .9})
        # self.bt1 = Button(text='Procure o Arquivo', size_hint=[.3, .1], pos_hint={"x": .35, "y": .9}, on_press=self.interface_procura)
        self.bt1.bind(on_press=lambda a='' : self.interface_procura())
        self.add_widget(self.bt1)


    def interface_procura(self):

        global procura_arquivo_parent

        # self.novo = ToggleButton(text='Male', group='sex', pos_hint={"x": .35, "y": .6}, size_hint=[.3, .1])

        self.procura_arquivo = FileChooserListView(pos_hint={"x": .05, "y": .1}, size_hint=[.9, .3], filters=["*.xlsx"])

        self.btok = Button(text="OK", pos_hint={"x": .35, "y": .8}, size_hint=[.3, .1], on_press=lambda a='': self.seleciona_arquivo())

        print(self.procura_arquivo.parent)


        if procura_arquivo_parent == "None":


            # self.add_widget(self.novo)
            self.add_widget(self.btok)
            self.add_widget(self.procura_arquivo)



            procura_arquivo_parent = "Já exixte"






    def seleciona_arquivo(self):

        global procura_arquivo_parent, aviso_selecione_arquivo_parent

        # print(self.novo.state)

        if len(self.procura_arquivo.selection) == 1:

            str_caminho_do_arquivo = self.procura_arquivo.selection
            self.arquivo = pd.read_excel(str_caminho_do_arquivo[0])


            self.remove_widget(self.btok)
            self.remove_widget(self.procura_arquivo)
            if aviso_selecione_arquivo_parent != 'None':
                self.remove_widget(self.aviso_selecione_arquivo)

            procura_arquivo_parent = "None"

            self.monta_informacao()
        else:
            if aviso_selecione_arquivo_parent == 'None':
                self.aviso_selecione_arquivo=Label(text='Selecione um arquivo', pos_hint={"x": .35, "y": .7}, size_hint=[.3, .1])
                self.add_widget(self.aviso_selecione_arquivo)
                aviso_selecione_arquivo_parent = "Já exixte"
                print('selecione um arquivo')


    def monta_informacao(self):
        global infos
        print(self.arquivo.iloc[1, 6])
        # def __init__(self, num_orc, num_nf, cabc, desct, vencm, serv):
        infos=Info(num_orc = self.arquivo.iloc[1, 6], num_nf = self.arquivo.iloc[11, 2], cabc = self.arquivo.iloc[10, 1], desct = self.arquivo.iloc[34, 6], vencm = self.arquivo.iloc[34, 2])

        servc=[]
        for g in range (12, 32):
            di={'servico' : str(self.arquivo.iloc[g, 1]), 'valor' : self.arquivo.iloc[g, 6]}
            if str(self.arquivo.iloc[g, 1]) != 'nan' and str(self.arquivo.iloc[g, 6]) != 'nan':
                servc.append(di)

        for n in range (0, len(servc)):
            print(servc[n]['servico'], end='==')
            print(servc[n]['valor'])



        infos.serv=servc

        print(infos.serv)

        self.interface_servicos()
    def interface_servicos(self):

        global infos

        for n in range (0, len(infos.serv)):
            # print(infos.serv[n]['servico'], end='==')
            # print(infos.serv[n]['valor'])
            self.novo = Label(text=infos.serv[n]['servico'], pos_hint={"x": .1, "y": .7-(n/20)}, size_hint=[.3, .05])
            self.novo2 = Switch(pos_hint={"x": .3, "y": .7 - (n / 20)}, size_hint=[.3, .05])
            # self.novo3 = Switch(text='123')
            self.add_widget(self.novo)
            self.add_widget(self.novo2)

class Tela(App):
    def build(self):
        return Prog()


Tela().run()
