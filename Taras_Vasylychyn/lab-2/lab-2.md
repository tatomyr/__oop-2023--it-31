## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №2
# "Variables and Types, Lists, Basic Operators, String Formatting, Basic String Operations, Dictionaries."



| Виконав: студент групи ІТ-31 Василишин Тарас |
|----------------------------------------------|
| Перевірив: Татомир Андрій                    |


**Мета: ознайомлення з такими темами: Variables and Types, Lists, Basic Operators,
String Formatting, Basic String Operations, Dictionaries.**


Хід роботи

1. Заходжу на сайт https://www.learnpython.org/


2. Знайомлюся з темою Variables and Types. 


3. Виконую задачу з цієї теми. [Exercise](./lab-2.py)


4. Далі переходжу до теми Lists. Знайомлюся зі списками, як їх заповнювати ```(mylist = []; mylist.append(1))```,
та як витягувати ```(print(mylist[0]))``` з них інформацію.


5. Наступна тема Basic Operators. В цій темі розповідається про основні арифметичні операції. 
Наприклад: оператор модуля (%), який повертає цілу остачу від ділення. дивіденд % дільник = залишок.
```
(input: remainder = 11 % 3)(output: 2)
```
Використання двох символів множення створює відношення степенів.
```
(input: squared = 7 ** 2(output: 49)
```
Python також підтримує множення рядків для формування рядка з повторюваною послідовністю:
```
(input: lotsofhellos = "hello" * 10)(output: hellohellohellohellohellohellohellohellohellohello)
```

6. Далі String Formatting. 

*Here are some basic argument specifiers you should know:*

*%s - String (or any object with a string representation, like numbers)*

*%d - Integers*

*%f - Floating point numbers*

*%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.*

*%x/%X - Integers in hex representation (lowercase/uppercase)*

7. Наступна тема Basic String Operations.

Можна дізнатися довжину рядка:
```(input: astring = "Hello world!"; print(len(astring)))(output: 12)```
Також можна дізнатися індекс певного символу:
```(input: astring = "Hello world!"; print(astring.index("o")))(output: 4)```

10. Остання тема Dictionaries. 

Словник — це тип даних, подібний до масивів, але він працює з ключами та значеннями замість індексів.
До кожного значення, що зберігається в словнику, можна отримати доступ за допомогою ключа, який є будь-яким типом об’єкта (рядок, число, список тощо), замість використання його індексу для адресації.

```
(input: phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781} for name, number in phonebook.items(): print("Phone number of %s is %d" % (name, number)))
``` 
```
(otput: Phone number of Jill is 947662781 Phone number of Jack is 938377264 Phone number of John is 938477566)
```
## Висновки. 
На даній лабораторній роботі я познайомився з такими темами як Variables and Types, Lists, Basic Operators,
String Formatting, Basic String Operations, Dictionaries. Для кожної з цих тем познайомився з кусочками коду, щоб
зрозуміти детальнішу суть кожної з команд. Команди я записав у звіті, а також те, що виводиться після їхнього виконання.
Також дещо застосував і засвоїв на практиці.
