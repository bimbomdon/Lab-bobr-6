import math

def vvod(vybor):
    """Спрашивает размеры фигуры. vybor — это цифра из меню."""
    if vybor == "1":
        return "круг", (float(input("Радиус: ")),)

    if vybor == "2":
        while True:
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            # Проверяем, что треугольник существует
            if a + b > c and a + c > b and b + c > a:
                return "треугольник", (a, b, c)
            print("Ошибка: такого треугольника нет. Попробуйте снова.")

    return "прямоугольник", (float(input("Ширина: ")), float(input("Высота: ")))


def ploshad(tip, d):
    """Считает площадь по типу фигуры."""
    if tip == "круг":
        return math.pi * d[0] ** 2
    if tip == "треугольник":
        a, b, c = d
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    return d[0] * d[1]


def vyvod(tip, s):
    """Печатает результат."""
    print("Площадь", tip, "=", round(s, 4))


# Главный цикл
while True:
    print("\n1-круг  2-треугольник  3-прямоугольник  0-выход")
    vybor = input("Выбор: ")

    if vybor == "0":
        break

    # Передаём выбор внутрь функции ввода
    tip, d = vvod(vybor)
    vyvod(tip, ploshad(tip, d))