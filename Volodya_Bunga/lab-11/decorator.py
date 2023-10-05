def my_decorator(func):
    def wrapper():
        while True:
         x = int(input("Tell me your year of birthday"))
         func()
         if x >=2023:
             print(" try again")
         else:
           y = 2023 - x
           print(f"You are {y} years old")
           break
         
    return wrapper


@my_decorator
def say_hello():
    print("Привіт!")


say_hello()