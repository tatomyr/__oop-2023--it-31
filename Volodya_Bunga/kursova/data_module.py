from version_2 import Cow
from version_2 import Chicken
import sqlite3


class Database:
    
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    
    def add_cow(self, cow):
        self.cursor.execute("INSERT INTO cows (id, name, date, howmuch, animal_id) VALUES (?, ?, ?, ?, ?)", (cow.id, cow.name, cow.a_name1, cow.much, cow.dep_numb))
    def remove_chicken(self,value):
        query = f"DELETE FROM chickens WHERE id = ?"
        self.cursor.execute(query,(value,))
    def remove_cow(self,value):
        query = f"DELETE FROM cows WHERE id = ?"
        self.cursor.execute(query,(value,))
        
    def add_chicken(self,chicken):
        self.cursor.execute("INSERT INTO cows (id, name, date, howmuch, animal_id) VALUES (?, ?, ?, ?, ?)", (chicken.id, chicken.name, chicken.a_name, chicken.much, chicken.dep_numb))

    def get_all_chickens(self):
        self.cursor.execute("SELECT * FROM chickens")
        return self.cursor.fetchall()

    def get_all_cows(self):
        self.cursor.execute("SELECT * FROM cows")
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()

class UserInterface:
    
    def __init__(self, db_file):
        self.db = Database(db_file)
    
    def add_chicken(self):
        chicken= Chicken.from_input()
        self.db.add_chicken(chicken)
     
    def add_cow(self):
        
        cow = Cow.from_input()
        self.db.add_cow(cow)
        print("Datas added successfully!")
        
    def remove_chickens(self):


        id = input("введіть ід (наприклад: 2):\n")
        self.db.remove_chicken(id)

    def remove_cows(self):


        id = input("введіть ід (наприклад: 2):\n")
        self.db.remove_cow(id)
    
    def view_cows(self):
        cows = self.db.get_all_cows()
        for cow in cows:
            print(cow)

        if not cows:
            print("No cows in the database.")

    def view_chickens(self):
        chickens = self.db.get_all_chickens()
        for chicken in chickens:
            print(chicken)

        if not chickens:
            print("No chickens in the database.")
    
    def close_database(self):
        self.db.close()
ui = UserInterface("/run/media/vova/Новий том/db/da.db")


def choice():
    
    while True :
        x = str(input(' Виберіть 1 - якщо ви хочете записати дані про корів \nВиебріть 2 - якщо ви хочете записати дані про курей\n Якщо ви хочете вийти виберіть - 3\n'))
        if  "1"==x :
             print("Ви вибрали Корову , введіть дані ")
             ui.add_cow()
             break
        elif   '2' ==x :
             print("Ви вибрали курку, введіть дані ")
             ui.add_chicken()
             break
        elif x == '3':
            
            ui.close_database()
            break
        else :
            print("Такої тварини ще не добавлено")

def choose() :
    
     
     while True :
          print("Вас вітає програма <Лістер> для обліку тваринницької діяльності на даній фермі")
          print("Якщо ви хочете добавити інформацію введіть - 1\nякщо ви хочете переглянути інформацію введіь -2 : \nякщо ви хочете видалити дані введіть - 3\nЯкщо ви хочете вийти виберіть - 4\n   ")
          y = str( input(""))
          if y == '1':
               choice()
          elif y == '2':
               
               while True :
                    l = str(input("Якщо ви хочете переглянути дані Корів введіть -1 \nЯкщо ви хочете переглянути дані курей введіть -2 \nЯкщо ви хочете вийти виберіть - 3\n "))
                    if l =="1":
                         ui.view_cows()
                         break
                    elif l == "2":
                         ui.view_chickens()
                         break
                    elif l =='3':
                        ui.close_database()
                        break
                    else :
                         
                         print( "Введена невірний формат ,спробуйте ще раз"
                              )
          elif y == '3': 
               while True :
                x = str(input(' Виберіть 1 - якщо ви видалити дані про корів \nВиебріть 2 - якщо ви хочете видалити дані про курей\n Якщо ви хочете вийти виберіть - 3\n'))
                if  "1"==x :
                    print("Ви вибрали Корову ")
                    ui.remove_cows()
                    break
                elif   '2' ==x :
                    print("Ви вибрали курку, введіть дані ")
                    ui.remove_chickens()
                    break
                elif "3" ==x:
                    break
          elif x == '4':
            ui.close_database()
            break
            
                  
          else :
              print("Введено невірний формат,спробуйте ще раз")
              
          
choose()


