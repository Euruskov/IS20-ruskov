from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
1,12 вариант
a = int(input ("Введите число:"))
b = int(input ("Введите число:"))
c = int(input ("Введите число:"))
x = 0
if int(a) < 0:
    x = x + 1
if int(b) < 0:
    x = x + 1
if int(c) < 0:
    x = x + 1
print(x)

2,13 вариант
a = int(input ("Введите число:"))
b = int(input ("Введите число:"))
c = int(input ("Введите число:"))
x = 0
if int(a) > 0:
    x = x + 1
if int(b) > 0:
    x = x + 1
if int(c) > 0:
    x = x + 1
print(x)

3,14 вариант
a = int(input ("Введите число:"))
b = int(input ("Введите число:"))
c = int(input ("Введите число:"))
x = 0
if int(a) %2 != 0:
    x = x + 1
if int(b) %2 != 0:
    x = x + 1
if int(c) %2 != 0:
    x = x + 1
print(x)

4,15 вариант
def find_divisors(a, b, c, k):
    divisors = []
    for i in range(1, k+1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            divisors.append(i)
    return divisors

a = int(input ("Введите число a:"))
b = int(input ("Введите число b:"))
c = int(input ("Введите число c:"))
k = int(input ("Введите число k:"))

result = find_divisors(a, b, c, k)

print(f"Делителями чисал {a}, {b}, {c} являются: {result}")

5,20 вариант
a = int(input ("Введите первое число:"))
b = int(input ("Введите второе число:"))

if a != b:
    max_number = max(a,b)
    a = max_number
    b = max_number
else:
    a = 0
    b = 0

print("Первое число после замены:", a)
print("Первое число после замены:", b)

6,16 вариант
def daisy_game(petals):
    if petals % 2 ==0:
        return "Она тебя не любит"
    else:
        return "Она тебя любит"

petals = int(input("Введите количетсво лепестков: "))

result = daisy_game(petals)

print(result)

7,17 вариант
a = int(input ("Введите число:"))
b = int(input ("Введите число:"))
c = int(input ("Введите число:"))

count = 0
if a % 2 == 0:
    count += 1
if b % 2 == 0:
    count += 1
if c % 2 == 0:
    count += 1

print(f"Количество четных чисел среди a,b,c: {count}")

8,18 вариант

def check_date():
    day = int(input("Введите день (от 1 до 31): "))
    month = int(input("Введите месяц (от 1 до 12):"))

    if day < 1 or day > 31:
        print("Неверно введен день")
    elif month < 1 or month > 12:
        print("Неверно введен месяц")
    else:
        print("Дата введена корректно")

check_date()
9,19 ВАРИАНТ
t = int(input ("Введите число:")
if int(t) > 60:
        print("Пожароопасная ситуация")

10 вариант
slovo = str(input())
x = len(slovo)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if slovo [x - i] == slovo[i]
        i += 1
else:
    k = 1
    break
if k == 1:
    print("no")
else:
    print("yes")

11 вариант

print("0 в качестве знака операции"
      "\nзавершит работу программы\n")

while True:
    s = input("Знак (+, -, *, /): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input("a = "))
        b = float(input("b = "))
        if s == '+':
            print("%.2f" % (a + b))
        elif s == '-':
            print("%.2f" % (a - b))
        elif s == '*':
            print("%.2f" % (a * b))
        elif s == '/':
            if b != 0:
                print("%.2f" % (a / b))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
            
            
            
            
