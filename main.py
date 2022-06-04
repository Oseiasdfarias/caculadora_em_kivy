import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.config import Config 
Config.set('graphics', 'width', '380') 
Config.set('graphics', 'height', '480')

class MyBoxLayout(BoxLayout):
    calculo = StringProperty("0")

    def remover(self, valor):
        if valor:
            valor = valor[:-1]
            self.calculo = valor


    def calcular(self, valor):
        valor1 = valor.replace(",", ".")
        valor1 = valor1.replace("sqrt", "math.sqrt")
        valor1 = valor1.replace("sen", "math.sin")
        valor1 = valor1.replace("cos", "math.cos")
        valor1 = valor1.replace("^", "**")
        print(valor1)
        if valor:
            try:
                vl = eval(valor1)
                
                if type(vl) == float: 
                    vl1 = f"{vl:.4f}".replace(".", ",")
                    print(vl1)
                else:
                    vl1 = str(vl).replace(".", ",")
                self.calculo = vl1
                
            except Exception:
                self.calculo = "Erro! Tente Novamente"


class MainApp(App):
    def build(self):
        return MyBoxLayout()

MainApp().run()