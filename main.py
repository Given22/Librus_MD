from Lib import *
import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import ThreeLineListItem

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty

from jwk_librus import MyLibrus

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class tajneAkta(MDApp):
    login = ObjectProperty(None)
    password = ObjectProperty(None)
    nr = ObjectProperty(None)

    dialog = None

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Gray'
        Window.size = (1080 / 3 , 2244 /3)
        return Builder.load_file('gui.kv')

    def logIn(self):
        error = MDDialog(title='Nie zalogowano!', text='Wystąpił błąd i nie udało się zalogować do librusa', size_hint=[.7,.5])

        login = self.root.ids.login.text
        password = self.root.ids.haslo.text
        nr = 0
        if not self.root.ids.nr.text == '':
            nr = int(self.root.ids.nr.text)

        self.lib = MyLibrus(login, password, nr)

        if self.lib.polacz():
            self.nieobecnosciList()
            self.numerek(nr)
        else:
            self.show_alert_dialog('Nie zalogowano!')

    def nieobecnosci(self, data):
        nieobecnosc = []
        j = 0
        print(data)
        for s in data:
            nieobecnosc.append([])
            if 'Teacher' in s:
                for x in s['Teacher']:
                    nieobecnosc[j].append(s['Teacher'][x])
                del s['Teacher']
            for x in s:
                nieobecnosc[j].append(s[x])
            j += 1
        return nieobecnosc

    def nieobecnosciW(self, data):
        nieobecnosc = []
        j = 0
        for s in data:
            nieobecnosc.append([])
            if 'Teacher' in s:
                for x in s['Teacher']:
                    nieobecnosc[j].append(s['Teacher'][x])
                del s['Teacher']
            for x in s:
                nieobecnosc[j].append(s[x])
            j += 1
        return nieobecnosc

    def nieobecnosciList(self):
        nieobecnosc = self.nieobecnosci(self.lib.nieObecnosci())

        for i in nieobecnosc:
            self.root.ids.nieobecnosci_1.add_widget(
                ThreeLineListItem(text=' '.join(i[:2]), secondary_text=i[2], tertiary_text=' '.join(i[3:]))
            )

        nieobecnosc2 = self.nieobecnosciW(self.lib.nieObecnosci(True))[:-(len(nieobecnosc))] + nieobecnosc

        for i in nieobecnosc2[::-1]:
            self.root.ids.nieobecnosci_2.add_widget(
                ThreeLineListItem(text=' '.join(i[:2]), secondary_text=i[2], tertiary_text=' '.join(i[3:]))
            )

    def numerek(self,nr):
        numerek = self.lib.numerek()
        self.root.ids.numerek.text = str(numerek)
        self.root.ids.numerek.font_style = 'H1'
        if numerek == nr:
            self.show_alert_dialog('Masz Szczęśliwy numerek')

    def show_alert_dialog(self, text):
        if not self.dialog:
            self.dialog = MDDialog(text=text)
        self.dialog.open()

tajneAkta().run()
