# print(whatsapp)                                     
# print("telegram")
# print(10+10)
# print(2374568723465873456347+6573467837846579)
# print(20-10)
# print(15*15)
# print(10/5)
# print(10//3)
# print("fdgiklhj")
# print(10==111)
# print(10==10)
# print(10=>9
# tima=tank 
# print(tima)
# tima="itrun" 
# print(tima)
# print("tims")
# print(67*87)
# tima=home 
# print(tima)
# tima1="famas "
# tima2="aug "
# tima3="awm " 
# print(tima1+tima2+tima3)
# print("int")

# hy= "fly"

# tim= hy
# print(tim)

# tim= "hi, i'm tim" 
# print(tim) 


# tim= """В Python есть четыре вида числового типа данных: int (целое число) long (длинное целое число [может быть представлено в восьмеричной или шестнадцатеричной системе исчисления]) float (число с плавающей точкой: -0.2, 0.0, 3.14159265 и т.22 сент. 2014 г."""
# print(tim)

# feat="""В 2011 году в состав минской студии разработки Wargaming вошла команда DAVA Consulting. А уже через три года свет увидел World of Tanks Blitz — мобильный ММО-экшен, посвященный танковым сражениям середины ХХ века. 26 июня игра отметила свой первый день рождения. В честь этого журнал CG Magic пообщался с художниками, которые отвечали за разработку графического контента World of Tanks Blitz."""       
# print(feat)

# no= "lenina"
#     #0123456
# print(no[1])
# name = input("Введите свое имя ")
# print("Добро пожаловать", name)
# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# print(num1 + num2)
# a = 1000
# b = 500
# if a > b:
    # print("A больше B")
# else:
    # print("B больше A")

# wer
# year = int (input("Year: "))
# month  = int (input("Month: "))
# day = int (input("Day: "))
# 
#     if month >= 1 and month <= 12:
#         if day >= 1 and day <= 30:
#             print("Правif year >= 1 and year <= 2022:ильная дата")
#         else:
#             print("Неправильная дата")
#     else:
#         print("Неправильный месяц")
# else:
#     print("Неправильный год")
# names = ("Abbas", "Talgat", "Gold")
# print (tuple(names))

# playlist = ["Французский Поцелуй", "Неболей", "Камин", "Пустота", "Влюбилась В Пацана", "Поболело и

# loglin = "Gold"
# Password = "Rolton"


# klon = int (input("Password: "))
# Password = int (input("Password: "))

# cars = {"Audi", "BMV", "TESLA", "Rolls Royce" }
# cars. add("test")
# print (cars) 
# cars.pop()  
# print (cars) 
# cars.remove("TESLA")
# print (cars)

# for i in cars:
#     print (i)

# cars = frozenset ([1, 2, 3, 4, 4, 4, 4])
# for i in cars:
#     print (i)

# numbers = []
# for i in range(1, 1000001):
#     numbers.append(i)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(numbers)

# numbers = [1, 2, 3, 4, 5,]

# student = {"Name" : "Muntasir", "age": 18, "study" : "IT RUN"}
# print (len(student))

# student = {"Name" : "Muntasir", "age": 18, "study" : "IT RUN"}
# print (student)

# student = {"Name" : "Muntasir", "age": 18, "study" : "IT RUN"}
# del student["age"]
# print (student)

# student = {"Name" : "Muntasir", "age": 18, "study" : "IT RUN"}
# student['study'] = "OSH MU"
# print (student)

# student= {"Name" : "Muntasir", "age": 18, "study" : "IT RUN"}
# print(student.keys())
# print(student.values())
# print(student.get('color'))
# print(student.items())
# for key, value in student.items():
    # print(key,value)

# contact = {"Abbas" : 77111111111 }
# while True:
#     Command = input("1 - Искать, 2 - Добавить, 3 - Удалить, 4 - обновить номер, 5 - Посмотреть все контакты: ")
#     if Command == "1":
#         find_num = input("Какой контакт вы хотите найти?")
#         if find_num.title() in contact:
#             print("Есть", contact[find_num.title()])
#         else:
#             print("Такого нету")
#     elif Command == "2":
#         add_name = input("Кого добавить?")
#         add_num = input("Введите номер: ")
#         contact.setdefault(add_name, add_num)
#         print("Контакт успешно добавлен")
#     elif Command == "3":
#         del_name = input ("Какое имя удалить? ")
#         if del_name in contact:

#             contact.pop(del_name)
#             print("Имя успешно удален")
#         else:
#             print("такого имени нету")
#     elif Command == "4":
#         update_name = input("какого пользователя обновить? ")
#         if update_name in contact:
#             update_num = input("Обновить номер ")
#             contact[update_name] = update_num
#             print ("Номер контакта успешно обновлен")
#         else:
#             print("такого нету")
#     elif Command == "5":
#         for name, number in contact.items():
#             print(f"{name} - {number}")
#     else:
#         print("Такой комманды нет")


        
# from datetime import datetime
 
# def toDate(date):
#    return datetime.strptime(date, "%H:%M:%S")
 
# def diff(start, end):
#    delta = (toDate(end) - toDate(start)).seconds
#    delta, seconds = divmod(delta, 60)
#    delta, minutes = divmod(delta, 60)
#    return "{} {} {}".format(delta, minutes, seconds)
   
# if __name__ == "__main__":
#    print(diff("1:50:50", "2:10:10"))
#    print(diff("0:59:59", "11:11:11"))
#    print(diff("11:28:47", "22:12:2"))

# a = 100
# b = 10
# if a > b:
#     print("a больше всех")
# else:
#     print("a не больше всех")

# a = 100
# b = 10

# res = "a больше всех" if a > b else "a меньше всех"
# print (res)

# a = 100
# b = 10

# print ("A больше всех" if a > b else "A меньше всех")



# a = 100
# b = 10
# c = 1000
# res = a if a > b and a > c else b if b > a and b > c else c
# print (res)

# a = 100
# b = 10
# c = 1000
# d = 5000
# res = a if a > b and a > c and a > d else b if b > a and b > c and b 

# number = int(input("Number: "))
# if number % 2 == 0:
#     print ("Четное")
# else:
#     print ("Нечетное")

# number = int(input("Number: "))
# print ("Четное" if number % 2 == 0 else "Нечетное")

# number = int(input("Number: "))
# print (("Четное", "Нечетное")[number % 2])

# My_passwords = ["asdasdads", "12345678"]
# user_input = input("Введите пароль: ")
# if user_input in My_passwords:
#     print ("Пароль верный")
# else:
#     print ("Неверный пароль")

# nums = []
# for i in range(0, 101):
# 		nums.append(i)

# print(nums)

# nums = [i for i in range(0, 101)]
# print(nums)

# nums = []
# for i in range(0, 101):
# 	  if i % 2 == 0:
#         nums.append(i)

# print(nums)

# num = [i for i in range(0, 101) if i % 2 == 0]

# petrol = {
# 	'Ai 100': 50,
# 	'Ai 95': 55,
# 	'Ai 92': 50,
# 	'Ai 80': 40,
# }
# new_petrol = { k:v + 10 for k, v in petrol.items() }
# print(new_petrol)

# petrol = {
# 	'Ai 100': 50,
# 	'Ai 95': 55,
# 	'Ai 92': 50,
# 	'Ai 80': 40,
# }
# new_petrol = {}
# for key, value in petrol.items():
#    new_petrol[key] = value + 10

# print(new_petrol)

# petrol = {
# 	'Ai 100': 50,
# 	'Ai 95': 55,
# 	'Ai 92': 50,
# 	'Ai 80': 40,
# }
# for key, value in petrol.items():
#    if value == 50:
#        petrol[key] = value + 5

# print(petrol)

# num = [i for i in range(10)]
# print(num)

# lst = []
# for i in range (10):
#     if i % 2 == 0:
#         lst.append(i)
# print (lst)

# def names(*args):
#     print (args)

# names ("Kurmanbek", "Muntasir", "Diana", "Faha", "IT RUN",)

# def elon_mosk(name, *company):
#     print (name)
#     for i in company:
#         print(i)

# elon_mosk("Elon", "tesla", "spase x" "paypal", "starlink")

# def traslate(**words):
#     for k, v in words.items():
#         print (k, v)
# traslate(USA = "США", KYRGYZSTAN = "Кыргызстан")



    