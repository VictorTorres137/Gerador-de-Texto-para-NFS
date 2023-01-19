# from pandas import *
import pandas as pd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import *


# from openpyxl


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
        self.procura_arquivo = FileChooserListView(pos_hint={"x": .05, "y": .1}, size_hint=[.9, .3], filters =["*.xlsx"])

        self.btok = Button(text="OK", pos_hint={"x": .35, "y": .8}, size_hint=[.3, .1], on_press=lambda a='': self.seleciona_arquivo())
        # print(self.FloatLayout)
        self.add_widget(self.btok)
        self.add_widget(self.procura_arquivo)

        # return self.procura_arquivo



    def seleciona_arquivo(self):

        str_caminho_do_arquivo = self.procura_arquivo.selection

        self.arquivo = pd.read_excel(str_caminho_do_arquivo[0])

        # print(arquivo.iloc[20, 0])

        self.remove_widget(self.btok)
        self.remove_widget(self.procura_arquivo)

        # infos=Info(num_orc = self.arquivo.iat[1, 6])
        # print(infos.num_orc)
        # for x in range(0,38):
        #     for y in range(0, 7):
        #         if str(self.arquivo.iat[x, y]) != "nan":
        #             print(self.arquivo.iat[x, y])
        #             print(f'{x},{y}')


        print(self.arquivo)
        self.monta_informacao()



    def monta_informacao(self):
        print(self.arquivo.iloc[1, 6])
        # def __init__(self, num_orc, num_nf, cabc, desct, vencm, serv):
        infos=Info(num_orc = self.arquivo.iloc[1, 6], num_nf = self.arquivo.iloc[11, 2], cabc = self.arquivo.iloc[10, 1], desct = self.arquivo.iloc[34, 6], vencm = self.arquivo.iloc[34, 2])

        servc=[]
        for g in range (12, 32):
            di={'servico' : self.arquivo.iloc[g, 1], 'valor' : self.arquivo.iloc[g, 6]}
            if str(self.arquivo.iloc[g, 1]) != 'nan' or str(self.arquivo.iloc[g, 6]) != 'nan':
                servc.append(di)

        for n in range (0, len(servc)):
            print(servc[n]['servico'], end='==')
            print(servc[n]['valor'])

        infos.serv=servc

        print(infos.serv)


class Tela(App):
    def build(self):
        return Prog()


Tela().run()
