import math

# ===== ВВОД =====

def vvod():
    """Спрашивает коэффициенты a, b, c."""
    print("Решение квадратного уравнения ax² + bx + c = 0")
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        return a, b, c
    except ValueError:
        print("Ошибка: нужно ввести числа.")
        return None

# ===== РАСЧЁТ =====

def raschet(a, b, c):
    """Считает корни. Возвращает тип ответа и значения."""
    if a == 0:
        return "net_korney", None # Это не квадратное уравнение

    # Дискриминант
    d = b * b - 4 * a * c

    if d < 0:
        return "net_korney", d
    elif d == 0:
        x = -b / (2 * a)
        return "odin_koren", x
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        return "dva_kornya", (x1, x2)

# ===== ВЫВОД =====

def vyvod(tip, resultat):
    """Печатает ответ в зависимости от типа."""
    if tip == "net_korney":
        if resultat is None:
            print("Коэффициент 'a' не может быть равен нулю.")
        else:
            print("Корней нет, так как дискриминант < 0.")
    elif tip == "odin_koren":
        print("Один корень: x =", round(resultat, 4))
    elif tip == "dva_kornya":
        x1, x2 = resultat
        print("Два корня: x1 =", round(x1, 4), ", x2 =", round(x2, 4))

# ===== ГЛАВНАЯ ПРОГРАММА =====

koef = vvod()

if koef is not None:
    a, b, c = koef
    tip, res = raschet(a, b, c)
    vyvod(tip, res)