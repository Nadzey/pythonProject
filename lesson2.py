import datetime
# class
first_name = input("Fill in your name: ")
last_name = input("Fill in your last name: ")
sex = input("Fill in your sex: ")
country = input("Fill in your country: ")

print("Hi!", first_name)

a = 1
b = 20
c = -90

print(type(a))
print(type(b))
print(type(c))

a = b + c
print(a)
print(type(a))

x = a/b
print(x)
print(type(x))

# целочисленное деление //
y = b // c
print(b // c)
print(type(y))

# остаток
f = a % c
print(f)
print(type(f))

# class 'int' тип данных который предпологается

# cortege
date = (6, 'oktober', 2022)
print(date[0])

# преобразование динамическая типизация
print(float(1))
print(int(1.0))

# списки []

s = [1, 'kate', (1, 'a'), 'new']
s.append(16)
print(len(s))
print(s.index('new'))

# homework
# 2
banks = {'SBER': 3.2, 'VTB': 2.4, 'ALFA': 4.92, 'PRIOR': 3.0}

money = int(input("Enter amount: "))

sum_list = []

for bank, percent in banks.items():
    sum_list.append(int(money * percent / 100))

print(sum_list)


# 3
year = int(input("Fill in your year of birth: "))
month = int(input("Fill in your month of birth: "))
day = int(input("Fill in your day of birth: "))

birthdate = datetime.date(year, month, day)
today = datetime.date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

print("Вам", age, "лет")
