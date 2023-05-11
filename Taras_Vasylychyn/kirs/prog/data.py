from main import Sunrise
from main import Eagles
import sqlite3
import pandas as pd

class Data:
    def __init__(self,base_file):
        self.conn = sqlite3.connect(base_file)
        self.cursor = self.conn.cursor()

    def add_sunrise(self,sunrise):
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

