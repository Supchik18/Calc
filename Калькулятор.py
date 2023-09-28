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
    while True:
        try:
            choice = int(input("Введите номер операции: "))
            break
        except ValueError:
            print ("Нужно ввести число, а не буквы")
    if choice == 1:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 + num2
            print("Результат:", result)
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 2:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 - num2
            print("Результат:", result)
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 3:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 * num2
            print("Результат:", result)
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 4:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 / num2
            print("Результат:", result)
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 5:
        try:
            num1 = float(input("Введите число: "))
            power = int(input("Введите степень: "))
            result = num1 ** power
            print("Результат:", result)
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 6:
        try:
            choice = int(input("Введите число "))
            print("Результат ",choice**0.5)
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 7:
        try:
            num = float(input("Введите число: "))
            result = num * 0.01
            print("Результат:", result)
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 8:
        try:
            num = int(input("Введите число: "))
            result = 1
            for i in range(1, num + 1):
                result *= i
            print("Результат:", result)
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 9:
        try:
            break
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 10:
        try:
            num = float(input("Введите число: "))
            result = math.sin(num)
            print("Результат:", result)
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 11:
        try:
            num = float(input("Введите число: "))
            result = math.cos(num)
            print("Результат:", result)
        except ValueError:
            print("Нужно ввести число,а не буквы")
    elif choice == 12:
        try:
            num = float(input("Введите число: "))
            result = math.tan(num)
            print("Результат:", result)
        except ValueError:
            print("Нужно ввести число,а не буквы")

