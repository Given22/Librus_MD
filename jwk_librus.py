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

    def nieObecnosci(self, wszystkie = False):
        tajne_akta = librus.get_teacher_free_days()

        def ToDate(text):
            text = text.split('-')
            return date(int(text[0]), int(text[1]), int(text[2]))

        if not wszystkie:
            actual = []
            for x in tajne_akta:
                if date.today() <= ToDate(x["DateTo"]):
                    actual.append(x)
            return actual
        else:
            return tajne_akta

    def numerek(self):
        return librus.get_lucky_number()