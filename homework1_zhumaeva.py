# Task 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 'hello'
b = 1
name = input('whats your name:')
age = int(input('whats your age again:'))
number = int(input('whats your favorite number:'))
print(a, b, name, age, number)

# Task 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# спользуйте форматирование строк.

time = int(input('input time in seconds:'))
hrs = time // 3600
min = (time - hrs * 3600) // 60
sec = time - (hrs * 3600 + min * 60)
print(f' formatted time is {hrs:02}:{min:02}:{sec:02}')

# Task 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('input number'))
n_sum = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print("n + nn + nnn = %d" % n_sum)

# Task 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


n = abs(int(input('input integer number:')))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print('maximum digit is:', max)
        break

# Task 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


revenue = int(input('input firm revenue:'))
costs = int(input('input firm costs'))

if revenue > costs:
    print('your firm is profitable')
    employees = int(input('input the number of employees:'))
    print(f'revenue per employee = {revenue / employees}')
elif revenue == costs:
    print('earnings equal to costs')
else:
    print('your firm is not profitable')

# Task 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('1st day distance in km:'))
b = int(input('total desired distance in km'))
total_days = 1
total_km = a
while total_km < b:
        a = a + 0.1 * a
        total_days += 1
        total_km = total_km + a
print(f"you will reach the goal on %.d day" % total_days)