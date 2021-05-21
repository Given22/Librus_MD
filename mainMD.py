from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.dialog import MDDialog

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty

from jwk_librus import MyLibrus


class tajneAkta(MDApp):
    login = ObjectProperty(None)
    password = ObjectProperty(None)
    nr = ObjectProperty(None)

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        Window.size = (1080 / 3, 2244 / 3)
        return Builder.load_file('ta_gui.kv')

    def logIn(self):
        error = MDDialog(title='Nie zalogowano!', text='Wystąpił błąd i nie udało się zalogować do librusa', size_hint=[.7,.5])

        login = str(self.root.ids.login.text)
        password = str(self.root.ids.haslo.text)
        nr = self.root.ids.nr.text

        lib = MyLibrus(str(login), str(password), nr)

        if lib.polacz():
            print('udało sie')

    def clear(self):
        ab = 1

tajneAkta().run()
