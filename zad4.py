import math

# ===== ВЫЧИСЛЕНИЯ =====

def sokrashenie(chislitel, znamenatel):
    """Сокращает дробь с помощью НОД."""
    # math.gcd ищет наибольший общий делитель
    delitel = math.gcd(chislitel, znamenatel)
    return chislitel // delitel, znamenatel // delitel


def slozhenie(a, b, c, d):
    """Сложение a/b + c/d."""
    ch = a * d + c * b
    zn = b * d
    return sokrashenie(ch, zn)


def vychitanie(a, b, c, d):
    """Вычитание a/b - c/d."""
    ch = a * d - c * b
    zn = b * d
    return sokrashenie(ch, zn)


def umnozhenie(a, b, c, d):
    """Умножение a/b * c/d."""
    ch = a * c
    zn = b * d
    return sokrashenie(ch, zn)


def delenie(a, b, c, d):
    """Деление a/b / c/d."""
    if c == 0:
        return "Ошибка: деление на ноль!"
    ch = a * d
    zn = b * c
    # Если знаменатель ушёл в минус, переносим минус наверх
    if zn < 0:
        ch = -ch
        zn = -zn
    return sokrashenie(ch, zn)


# ===== ВВОД =====

def vvod():
    """Спрашивает две дроби и действие. Возвращает их."""
    print("Введите первую дробь (числитель и знаменатель через пробел):")
    a, b = map(int, input().split())
    
    print("Введите вторую дробь:")
    c, d = map(int, input().split())
    
    print("Выберите действие: + - * /")
    deystvie = input()
    
    return a, b, c, d, deystvie


# ===== ВЫВОД =====

def vyvod(rezultat):
    """Печатает результат-дробь или сообщение об ошибке."""
    if type(rezultat) == str:
        print(rezultat)
    else:
        ch, zn = rezultat
        print("Результат:", ch, "/", zn)


# ===== ГЛАВНАЯ ПРОГРАММА =====

a, b, c, d, deystvie = vvod()

if deystvie == "+":
    vyvod(slozhenie(a, b, c, d))
elif deystvie == "-":
    vyvod(vychitanie(a, b, c, d))
elif deystvie == "*":
    vyvod(umnozhenie(a, b, c, d))
elif deystvie == "/":
    vyvod(delenie(a, b, c, d))
else:
    print("Неизвестное действие.")