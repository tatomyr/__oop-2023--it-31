
class Animal:
    def __init__(self,id, name,much,dep_numb):
      self.id = id
      self.name = name
      self.much = much
      self.dep_numb =dep_numb
    
      

class Cow(Animal):
    def __init__(self ,id,name,a_name1,much,dep_numb) :
        super().__init__(id,name,much,dep_numb)
        self.a_name1 = a_name1
    

    @classmethod
    def from_input(cls):
        id= input(" Введіть ваш id ")
        name = input("Введіть ваше ім'я ")
        a_name1 = input("Введіть коди корів за якими ви доглядаєте")
        much = input(" Введіть скільки літрів молока ви отримали")
        dep_numb = input("Введіть номер відділу(частини) в якій ви працюєте  ")
        return cls(id=id,name=name,a_name1=a_name1,much=much,dep_numb=dep_numb)
    


class Chicken(Animal):
    def __init__(self ,id,name,a_name,much,dep_numb) :
        super().__init__(id,name,much,dep_numb)
        
        self.a_name = a_name

        
    @classmethod
    def from_input(cls):
        id= input(" Введіть ваш id ")
        name = input("Введіть ваше ім'я ")
        a_name = input("Введіть кількість курей за якими ви доглядаєте")
        much = input(" Введіть скільки яєць ви отримали")
        dep_numb = input("Введіть номер відділу(частини) в якій ви працюєте  ")
        
        return cls(id=id,name=name,a_name=a_name,much=much,dep_numb=dep_numb)
class Animal_Factory:
    def create_animal(self,animal_type):
        if animal_type == "Cow":
            return Cow.from_input()
        elif animal_type == "Chicken":
            return Chicken.from_input()
        else:
            raise ValueError("Invalid animal type")
factory = Animal_Factory(
)
def choice():
    
    while True :
        x = str(input(' Виберіть 1 - якщо ви хочете записати дані про корів \nВиебріть 2 - якщо ви хочете записати дані про курей\n Якщо ви хочете вийти виберіть - 3\n'))
        if  "1"==x :
             print("Ви вибрали Корову , введіть дані ")
             factory = Animal_Factory()
             cow = factory.create_animal("Cow")
             break
        elif   '2' ==x :
             print("Ви вибрали курку, введіть дані ")
             chicken = factory.create_animal("Chicken")
             break
        elif x == '3':
            
            
            break
        else :
            print("Такої тварини ще не добавлено")


choice()
е



