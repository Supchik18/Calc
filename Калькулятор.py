import math

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Найти 1 процент от числа")
    print("8. Найти факториал числа")
    print("9. Выйти из программы")
    print("10. Синус")
    print("11. Косинус")
    print("12. Тангенс")

    choice = int(input("Введите номер операции: "))

    if choice == 1:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 + num2
        print("Результат:", result)
    elif choice == 2:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 - num2
        print("Результат:", result)
    elif choice == 3:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 * num2
        print("Результат:", result)
    elif choice == 4:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 / num2
        print("Результат:", result)
    elif choice == 5:
        num1 = float(input("Введите число: "))
        power = int(input("Введите степень: "))
        result = num1 ** power
        print("Результат:", result)
    elif choice == 6:
        num = float(input("Введите число: "))
        result = math.sqrt(num)
        print("Результат:", result)
    elif choice == 7:
        num = float(input("Введите число: "))
        result = num * 0.01
        print("Результат:", result)
    elif choice == 8:
        num = int(input("Введите число: "))
        result = 1
        for i in range(1, num + 1):
            result *= i
        print("Результат:", result)
    elif choice == 9:
        break
    elif choice == 10:
        num = float(input("Введите число: "))
        result = math.sin(num)
        print("Результат:", result)
    elif choice == 11:
        num = float(input("Введите число: "))
        result = math.cos(num)
        print("Результат:", result)
    elif choice == 12:
        num = float(input("Введите число: "))
        result = math.tan(num)
        print("Результат:", result)
    else:
        print("Некорректный номер операции. Попробуйте снова.")
