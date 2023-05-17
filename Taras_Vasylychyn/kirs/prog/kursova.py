from main import Sunrise
from main import Eagles
import sqlite3
import pandas as pd

class Data:
    def __init__(self, base_file):
        self.conn = sqlite3.connect(base_file)
        self.cursor = self.conn.cursor()

    def add_sunrise(self, sunrise):
        cursor = self.conn.cursor()
        while True:
            try:
                cursor.execute("INSERT INTO Sunrise(id,name,city,humanitarian,road) VALUES(?,?,?,?,?)",
                               (sunrise.id, sunrise.name, sunrise.city, sunrise.hum,sunrise.road))
                break
            except sqlite3.IntegrityError:
                sunrise.id = input("Такий id вже існує, введіть будь-яку букву.")

        self.conn.commit()

    def add_eagles(self,eagles):
        cursor = self.conn.cursor()
        while True:
            try:
                cursor.execute("INSERT INTO EaglesGroup(id,name,city,humanitarian,suces) VALUES(?,?,?,?,?)",
                               (eagles.id, eagles.name, eagles.city, eagles.hum, eagles.sucess))
                break
            except sqlite3.IntegrityError:
                eagles.id = input("Такий id вже існує, введіть будь-яку букву.")

        self.conn.commit()

    def watch_sunrise(self):
        self.cursor.execute("SELECT * FROM Sunrise")
        data = self.cursor.fetchall()
        columns = [description[0] for description in self.cursor.description]
        df = pd.DataFrame(data, columns=columns)
        return print(df.to_string())

    def watch_eagles(self):
        self.cursor.execute("SELECT * FROM EaglesGroup")
        data = self.cursor.fetchall()
        columns = [description[0] for description in self.cursor.description]
        df = pd.DataFrame(data, columns=columns)
        return print(df.to_string())

    def remove_eagles(self,value):
        query = f"DELETE FROM EaglesGroup WHERE id = ?"
        self.cursor.execute(query,(value,))

    def remove_sunrise(self, value):
        query = f"DELETE FROM Sunrise WHERE  id = ?"
        self.cursor.execute(query, (value,))



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

o = True

def choose ():
    print("\n Вас вітає додаток 'Волонтер'!\n"
          "Тут ви можете додавати та видаляти волонтерів зі своєї волонтерської організації, а також переглядати інформацію про них.\n"
          "Приємної роботи! ")
    while o == True:
        x = input("\n Якщо ви хочете переглянути дані введіть: 1\n Якщо ви хочете ввести дані введіть: 2\n Якщо ви хочете видалити дані введіть: 3\n Якщо ви хочете вийти введіть: 4\n ")
        match x :

            case"1":
                while True:
                    y = input("\n Якщо ви хочете переглянути дані волонтерської групи Sunrise введіть: 1 \n Якщо ви хочете переглянути дані волонтерської групи EaglesGroup введіть: 2 \n Якщо ви хочете вийти введіть: 3\n")
                    match y:
                        case "1":
                            print("\n Ви переглядаєте дані волонтерської організації Sunrise.\n")
                            intarface.watch_all_sunrise()
                            break
                        case "2":
                            print("\n Ви переглядаєте дані волонтерської організації EaglesGroup.\n")
                            intarface.watch_all_eagles()
                            break
                        case"3":
                            intarface.close()
                            break

            case "2":
                while o==True:
                    l = input(
                        "\n Якщо ви хочете ввести дані волонтерської групи Sunrise введіть: 1 \n Якщо ви хочете ввести дані волонтерської групи EaglesGroup введіть: 2\n Якщо ви хочете вийти введіть: 3\n")
                    match l:
                        case "1":
                         intarface.add_sunrise()
                         break
                        case"2":
                         intarface.add_eagles()
                         break
                        case "3":
                         intarface.close()
                         break
            case "3":
                while True:
                    r = input("\n Якщо ви хочете видалити волонтера з волонтерської групи Sunrise введіть: 1 \n Якщо ви хочете видалити волонтера з волонтерської групи EaglesGroup введіть: 2\n Якщо ви хочете вийти введіть: 3\n")
                    match r:
                        case'1':
                            intarface.remove_sunrise()
                            break
                        case '2':
                            intarface.remove_eagle()
                            break
                        case "3":
                            intarface.close()
                            break
            case"4":
                break

choose()



#
#
