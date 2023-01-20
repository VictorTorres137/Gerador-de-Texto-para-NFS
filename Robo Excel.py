# from pandas import *
import pandas as pd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import *


# from openpyxl
procura_arquivo_parent = aviso_selecione_arquivo_parent= "None"
lista_servicos=[]
lista_selecionados=[]
servc = []
string_final=str_servicos=''
valor_total = 0
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
        self.bt1.bind(on_press=lambda a='' : self.interface_procura())
        self.add_widget(self.bt1)


    def interface_procura(self):

        global procura_arquivo_parent

        self.procura_arquivo = FileChooserListView(pos_hint={"x": .05, "y": .1}, size_hint=[.9, .7], filters=["*.xlsx"])
        self.btok = Button(text="OK", pos_hint={"x": .35, "y": .8}, size_hint=[.3, .1], on_press=lambda a='': self.seleciona_arquivo())


        if procura_arquivo_parent == "None":

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
                aviso_selecione_arquivo_parent = "None"

            procura_arquivo_parent = "None"

            self.monta_informacao()
        else:
            if aviso_selecione_arquivo_parent == 'None':
                self.aviso_selecione_arquivo=Label(text='Selecione um arquivo', pos_hint={"x": .35, "y": .7}, size_hint=[.3, .1])
                self.add_widget(self.aviso_selecione_arquivo)
                aviso_selecione_arquivo_parent = "Já exixte"
                print('selecione um arquivo')


    def monta_informacao(self):
        global infos, servc
        print(self.arquivo.iloc[1, 6])
        # def __init__(self, num_orc, num_nf, cabc, desct, vencm, serv):
        infos=Info(num_orc = self.arquivo.iloc[1, 6], num_nf = self.arquivo.iloc[11, 2], cabc = self.arquivo.iloc[10, 1], desct = self.arquivo.iloc[34, 6], vencm = self.arquivo.iloc[34, 2])


        for g in range (12, 32):
            di={'servico' : str(self.arquivo.iloc[g, 1]), 'valor' : str(self.arquivo.iloc[g, 6]), 'checkbox': ''}
            if str(self.arquivo.iloc[g, 1]) != 'nan' and str(self.arquivo.iloc[g, 6]) != 'nan':
                servc.append(di)

        for n in range (0, len(servc)):
            print(servc[n]['servico'], end='==')
            print(servc[n]['valor'])


        infos.serv=servc

        print(infos.serv)

        self.interface_servicos()


    def interface_servicos(self):

        global infos, lista_servicos, servc
        self.texto_instrucao = Label(text="Digite o número do pedido e marque os serviços desejados", pos_hint={"x": .35, "y": .75}, size_hint=[.3, .05])
        self.input_pedido=TextInput(text='', pos_hint={"x": .35, "y": .7}, size_hint=[.3, .05])

        #
        # for k in range(0, len(infos.serv)):
        #     globals()[f"self.novo{str(k)}"] = Label()
        #     globals()[f"self.novo2{str(k)}"] = CheckBox()
        #
        #     # lista_servicos.append(globals()[f"self.novo{str(k)}"])
        #     lista_servicos.append(globals()[f"self.novo2{str(k)}"])



        for n in range(0, len(infos.serv)):

            globals()[f"self.novo{str(n)}"] = Label(text=infos.serv[n]['servico'], pos_hint={"x": .1, "y": .65-(n/20)}, size_hint=[.3, .05], color = (213, 12, 43, 1))
            # globals()[f"self.novo2{str(n)}"] = CheckBox(pos_hint={"x": .3, "y": .7 - (n / 20)}, size_hint=[.3, .05], active=lambda a=str(n): self.estado_switch(a))
            globals()[f"self.novo2{str(n)}"] = CheckBox(pos_hint={"x": .3, "y": .65 - (n / 20)}, size_hint=[.3, .05])



            self.add_widget(globals()[f"self.novo{str(n)}"])
            self.add_widget(globals()[f"self.novo2{str(n)}"])

        self.btok2 = Button(text="OK2", pos_hint={"x": .35, "y": .8}, size_hint=[.3, .1], on_press=lambda a='': self.estado_switch())
        # self.btok2=Button(text="OK2", pos_hint={"x": .35, "y": .8}, size_hint=[.3, .1], on_press=lambda a='': self.monta_string_final())
        self.add_widget(self.btok2)
        self.add_widget(self.input_pedido)
        self.add_widget(self.texto_instrucao)

    def estado_switch(self):
        global lista_servicos, str_servicos, servc, lista_selecionados, valor_total

    # Remove os Widgets
        for n in range(0, len(infos.serv)):

            self.remove_widget(globals()[f"self.novo{str(n)}"])
            self.remove_widget(globals()[f"self.novo2{str(n)}"])

        self.remove_widget(self.btok2)
        self.remove_widget(self.input_pedido)
        self.remove_widget(self.texto_instrucao)

#####
    # Preenche o valor das CheckBox
        for n in range(0, len(infos.serv)):
            infos.serv[n]['checkbox'] = globals()[f"self.novo2{str(n)}"].active


        print(infos.serv)

        self.texto_NFS=TextInput(text="", pos_hint={"x": .1, "y": .1}, size_hint=[.8, .8])
        self.add_widget(self.texto_NFS)

        for j in infos.serv:
            if j["checkbox"]:
                valor_total += int(j["valor"])

                str_servicos = f'{str_servicos}\n      ' \
                               f'=> {j["servico"]} == R${str(round(int(j["valor"]),2))} '
        print(str_servicos)
        print(valor_total)
        self.monta_string_final()
    def monta_string_final(self):

        global lista_servicos, string_final, valor_total



        string_final=f'*** {infos.cabc} ***' \
                     f'{str_servicos}\n' \
                     f'*** Valor Total R${round(valor_total,2)}'




        print(string_final)

class Tela(App):
    def build(self):
        return Prog()


Tela().run()
