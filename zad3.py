import math

# ===== ВЫЧИСЛЕНИЯ (по заданию) =====

def IsPrime(n):
    """Проверяет, является ли число n простым."""
    if n < 2:
        return False
    # Проверяем делители только до корня из n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def NextPrime(n):
    """Возвращает следующее простое число после n."""
    x = n + 1
    while not IsPrime(x):
        x += 1
    return x


def PrimeRange(a, b):
    """Возвращает список простых чисел в диапазоне от a до b включительно."""
    result = []
    for x in range(a, b + 1):
        if IsPrime(x):
            result.append(x)
    return result


# ===== ВВОД =====

def vvod():
    """Спрашивает у пользователя данные и возвращает их."""
    print("\n1 - Проверить, простое ли число")
    print("2 - Найти следующее простое число")
    print("3 - Вывести простые числа в диапазоне")
    
    vibor = input("Выбор: ")
    
    if vibor == "1":
        n = int(input("Введите число: "))
        return "1", n
    elif vibor == "2":
        n = int(input("Введите число: "))
        return "2", n
    elif vibor == "3":
        a = int(input("Начало диапазона: "))
        b = int(input("Конец диапазона: "))
        return "3", (a, b)
    else:
        return "0", None


# ===== ВЫВОД =====

def vyvod(vibor, rezultat):
    """Печатает результат в зависимости от выбора."""
    if vibor == "1":
        if rezultat:
            print("Число является простым.")
        else:
            print("Число НЕ является простым.")
    elif vibor == "2":
        print("Следующее простое число:", rezultat)
    elif vibor == "3":
        print("Простые числа в диапазоне:", rezultat)


# ===== ГЛАВНАЯ ПРОГРАММА =====

while True:
    vibor, dannye = vvod()
    
    if vibor == "0":
        break
        
    elif vibor == "1":
        vyvod(vibor, IsPrime(dannye))
        
    elif vibor == "2":
        vyvod(vibor, NextPrime(dannye))
        
    elif vibor == "3":
        a, b = dannye
        vyvod(vibor, PrimeRange(a, b))