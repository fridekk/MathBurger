import time
import cmath


def calculate(x, coefficients, operations):
    result = coefficients[0] * x
    for i in range(1, len(coefficients)):
        if operations[i - 1] == '+':
            result += coefficients[i] * x
        elif operations[i - 1] == '-':
            result -= coefficients[i] * x
    return result


print('                                                                  Привет, это MathBurger')
time.sleep(1)
print('Я могу помочь тебе с решением математических примеров')
time.sleep(1)
print()
print('Выбери номер задачи (1,2,3)')
main_task = input("'Задачи с х'  'Квадратные уравнения  'Неравенства'  "
                  )
print('Загрузка...')
time.sleep(1)
if main_task == '1':
    print('Вам нужно передать:')
    print('1) Кол-во значений')
    print('2) Значения. Каждое из них будет представлено в виде: x - 2, 3x, (может больше) сумма значений')
    time.sleep(2)
    print('Загрузка...')
    time.sleep(3)

    value_amount_input = int(input('Количество значений:  '))
    coefficients = []
    operations = []
    for i in range(value_amount_input):
        coefficient = int(input('Введи коэфицент для х: '))
        coefficients.append(coefficient)
        if i != 0:
            operation = input('Введи операцию (+ или -): ')
            operations.append(operation)
    x = int(input('Передайте x:  '))
    equation_sum = calculate(x, coefficients, operations)
    print('Сумма уравнения: ', equation_sum)


elif main_task == '2':
    print('Вам нужно передать коэффициенты a, b и c для квадратного уравнения вида ax^2 + bx + c = 0')
    a = float(input('Введите коэффициент a: '))
    b = float(input('Введите коэффициент b: '))
    c = float(input('Введите коэффициент c: '))

    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + cmath.sqrt(D)) / (2 * a)
        x2 = (-b - cmath.sqrt(D)) / (2 * a)
        print('У уравнения два решения: ', x1, ' и ', x2)
    elif D == 0:
        x = -b / (2 * a)
        print('У уравнения одно решение: ', x)
    else:
        print('У уравнения нет реальных решений')

    if D >= 0:
        print('Проверка через теорему Виета:')
        print('Сумма корней: ', -b / a)
        print('Произведение корней: ', c / a)


elif main_task == '3':
    print('Вам нужно передать коэффициенты a, b и c для неравенства вида ax^2 + bx + c > 0 или ax^2 + bx + c < 0')
    a = float(input('Введите коэффициент a: '))
    b = float(input('Введите коэффициент b: '))
    c = float(input('Введите коэффициент c: '))
    inequality = input('Введите знак неравенства (">" или "<"): ')

    D = b ** 2 - 4 * a * c

    if D >= 0:
        x1 = (-b - cmath.sqrt(D)) / (2 * a)
        x2 = (-b + cmath.sqrt(D)) / (2 * a)
        if a > 0:
            if inequality == '>':
                print('Решение неравенства: x < ', x1, ' или x > ', x2)
            else:
                print('Решение неравенства: ', x1, ' < x < ', x2)
        else:
            if inequality == '>':
                print('Решение неравенства: ', x1, ' < x < ', x2)
            else:
                print('Решение неравенства: x < ', x1, ' или x > ', x2)
    else:
        print('Неравенство не имеет решений в действительных числах')

else:
    print('Выберите варианты 1, 2 или 3')
