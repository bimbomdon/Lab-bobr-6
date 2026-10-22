# ===== ВЫЧИСЛЕНИЯ (рекурсия) =====

def stepen(a, n):
    """Возводит число a в степень n через рекурсию."""
    if n == 0:
        return 1
    return a * stepen(a, n - 1)


def faktorial(n):
    """Считает факториал числа n через рекурсию."""
    if n <= 1:
        return 1
    return n * faktorial(n - 1)


def fibonachchi(n):
    """Возвращает n-е число Фибоначчи через рекурсию."""
    if n <= 1:
        return n
    return fibonachchi(n - 1) + fibonachchi(n - 2)


# ===== ВВОД =====

def vvod():
    """Спрашивает, что считаем, и нужные числа."""
    print("1 - Степень")
    print("2 - Факториал")
    print("3 - Числа Фибоначчи")
    vibor = input("Выбор: ")

    if vibor == "1":
        a = float(input("Введите число a: "))
        n = int(input("Введите степень n: "))
        return "1", (a, n)
    elif vibor == "2":
        n = int(input("Введите число для факториала: "))
        return "2", n
    elif vibor == "3":
        n = int(input("Введите номер числа Фибоначчи: "))
        return "3", n
    else:
        return "0", None


# ===== ВЫВОД =====

def vyvod(vibor, rezultat):
    """Печатает результат в зависимости от выбора."""
    if vibor == "1":
        print("Результат возведения в степень:", round(rezultat, 4))
    elif vibor == "2":
        print("Факториал равен:", rezultat)
    elif vibor == "3":
        print("Число Фибоначчи:", rezultat)


# ===== ГЛАВНАЯ ПРОГРАММА =====

while True:
    vibor, dannye = vvod()

    if vibor == "0":
        break

    if vibor == "1":
        a, n = dannye
        # Проверяем, что степень не отрицательная (для простоты)
        if n < 0:
            print("Ошибка: степень должна быть неотрицательной.")
        else:
            vyvod(vibor, stepen(a, n))

    elif vibor == "2":
        if dannye < 0:
            print("Ошибка: факториал есть только у чисел >= 0.")
        else:
            vyvod(vibor, faktorial(dannye))

    elif vibor == "3":
        if dannye < 0:
            print("Ошибка: номер числа Фибоначчи должен быть >= 0.")
        else:
            vyvod(vibor, fibonachchi(dannye))