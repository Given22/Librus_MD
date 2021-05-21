from py_librus_api import Librus
import time
from datetime import date

librus = Librus()

class MyLibrus():
    def __init__(self, login, password, nr):
        self.login = login
        self.password = password
        self.nr = nr

    def logowanie(self):
        return librus.login(self.login, self.password)

    def polacz(self):
        return librus.make_connection(self.login, self.password)

    def czyZalogowano(self):
        if not librus.logged_in:
            if not librus.login(self.login, self.password):
                return False
            else:
                return True

    def nieObecnosci(self):
        tajne_akta = librus.get_teacher_free_days()

        def ToDate(text):
            text = text.split('-')
            return date(int(text[0]), int(text[1]), int(text[2]))

        actual = []
        for x in tajne_akta:
            if date.today() <= ToDate(x["DateTo"]):
                actual.append(x)

        data = [{'text': str(j)} for j in actual]

        nieobecnosc = ''

        for i in data:
            s = eval(i['text'])
            if 'Teacher' in s:
                for x in s['Teacher']:
                    nieobecnosc += str(s['Teacher'][x]) + " "
                del s['Teacher']
            for j in s:
                nieobecnosc += str(s[j]) + " "
            nieobecnosc += '\n'

        return nieobecnosc