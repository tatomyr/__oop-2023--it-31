class Facade:
    def __init__(self):
        self.had = Had()
        self.middle = Middle()
        self.legs = Legs()

    def createPerson(self):
        self.had.addHad()
        self.middle.addMiddle()
        self.legs.addLegs()


class Had:
    def addHad(self):
        print(' 0')


class Middle:
    def addMiddle(self):
        print('/|\\')


class Legs:
    def addLegs(self):
        print('/ \\')


# Код для первірки роботи патерну.

print("Ви хочете створити людину?(Так/Ні)")
answer = input()

if answer == "Так":
    facade = Facade()
    facade.createPerson()
elif answer == "Ні":
    print("Я все одно створю людину.")
    facade = Facade()
    facade.createPerson()
else:
    print("Ваша відповідь не валідна, але я все одно створю людину.")
    facade = Facade()
    facade.createPerson()
