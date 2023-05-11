from main import Sunrise
from main import Eagles
from data import Data
import sqlite3
import pandas as pd

class Ui:
    def __init__(self,base):
        self.base = Data(base)

    def remove_eagle(self):
        z = input("Введіть ід (наприклад: 1):\n")
        self.base.remove_eagles(z)

    def remove_sunrise(self):
        z = input("Введіть ід (наприклад: 1):\n")
        self.base.remove_sunrise(z)

    def add_sunrise(self):
        s_id = int(input("\n Введіть id волонтера: \n"))
        s_name = str(input("\n Введіть ім'я волонтера: \n"))
        s_city = str(input("\n Введіть місто куди прямує волонтер: \n"))
        s_hum = str(input("\n Введіть яку гуманітарну допомогу везе волонтер: \n"))
        s_road = str(input("\n Введіть кількість виїздів волонтера: \n"))
        sunrise = Sunrise(s_id, s_name, s_city, s_hum,s_road)
        self.base.add_sunrise(sunrise)

    def add_eagles(self):
        e_id = int(input("\n Введіть id волонтера: \n"))
        e_name = str(input("\n Введіть ім'я волонтера: \n"))
        e_city = str(input("\n Введіть місто куди прямує волонтер: \n"))
        e_hum = str(input("\n Введіть яку гуманітарну допомогу везе волонтер: \n"))
        e_sucess = str(input("\n Введіть стан волонтера (у дорозі, успішно доставив допомогу): \n"))
        eagles = Eagles(e_id, e_name, e_city, e_hum, e_sucess)
        self.base.add_eagles(eagles)

    def watch_all_sunrise(self):
        sunrises =self.base.watch_sunrise()
        return print(sunrises)

    def watch_all_eagles(self):
        eagles =self.base.watch_eagles()
        return print(eagles)

    def close (self):
        self.base.cursor.close()

intarface = Ui("D:\kirs\wolunteers.db")
