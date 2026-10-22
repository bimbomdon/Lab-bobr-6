# ===== ВЫЧИСЛЕНИЯ (РАБОТА СО СТРОКАМИ) =====

def WordCount(s):
    """Считает количество слов в строке."""
    # Разбиваем строку по пробелам и считаем куски
    slova = s.split()
    return len(slova)


def Reverse(s):
    """Переворачивает строку задом наперёд."""
    # Срез [::-1] читает строку с конца в начало
    return s[::-1]


def ToUpperFirst(s):
    """Делает первую букву каждого слова заглавной."""
    # title() делает заглавной первую букву каждого слова в строке
    return s.title()


def IsPalindrome(s):
    """Проверяет, является ли строка палиндромом."""
    # Оставляем только буквы и цифры, приводим к нижнему регистру
    ochishchennaya = "".join(c.lower() for c in s if c.isalnum())
    # Сравниваем строку с её перевёрнутой версией
    return ochishchennaya == ochishchennaya[::-1]


# ===== ВВОД =====

def vvod():
    """Спрашивает строку и действие."""
    print("1 - Количество слов (WordCount)")
    print("2 - Перевернуть строку (Reverse)")
    print("3 - Заглавные буквы (ToUpperFirst)")
    print("4 - Проверить на палиндром (IsPalindrome)")
    
    vibor = input("Выбор: ")
    s = input("Введите строку: ")
    
    return vibor, s


# ===== ВЫВОД =====

def vyvod(vibor, s, rezultat):
    """Печатает результат работы функции."""
    if vibor == "1":
        print("Количество слов:", rezultat)
    elif vibor == "2":
        print("Перевёрнутая строка:", rezultat)
    elif vibor == "3":
        print("С заглавными буквами:", rezultat)
    elif vibor == "4":
        if rezultat:
            print("Это палиндром!")
        else:
            print("Это НЕ палиндром.")


# ===== ГЛАВНАЯ ПРОГРАММА =====

vibor, stroka = vvod()

if vibor == "1":
    vyvod(vibor, stroka, WordCount(stroka))
elif vibor == "2":
    vyvod(vibor, stroka, Reverse(stroka))
elif vibor == "3":
    vyvod(vibor, stroka, ToUpperFirst(stroka))
elif vibor == "4":
    vyvod(vibor, stroka, IsPalindrome(stroka))
else:
    print("Неверный пункт меню.")