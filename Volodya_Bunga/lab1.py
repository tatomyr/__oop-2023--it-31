from math import sqrt

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))
d = b**2 - 4* a * c
def pr():
    print("___________________________________________________________")
    return 0
def pr1():
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
if d>0:
    x1 = (-b+sqrt(d))/2*a
    x2 = (-b-sqrt(d))/2*a
    pr()
    print("| Корені рівняння дорівнюють: x1 = " , round(x1,2)," || " "x2 = ",round(x2,2),'|')
    pr1()
elif d==0:
    x1 = (-b + sqrt(d)) / 2 * a
    x2 = (-b - sqrt(d)) / 2 * a
    pr()
    print("Корені рівняння дорівнюють: x1 = ", round(x1,2), "x2 = ", round(x2,2))
    pr1()
elif d<0:
    print("Коренів немає")