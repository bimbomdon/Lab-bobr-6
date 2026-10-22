def vvod():
    """Спрашивает числа через пробел. Возвращает список чисел."""
    while True:
        try:
            s = input("Введите числа через пробел: ")
            # Разбиваем строку на части и превращаем в числа
            chisla = [float(x) for x in s.split()]
            if len(chisla) > 0:
                return chisla
            print("Вы ничего не ввели.")
        except ValueError:
            print("Ошибка: нужно вводить только числа.")


def obrabotka(chisla):
    """Считает сумму, среднее, минимум, максимум и количество."""
    summa = sum(chisla)
    srednee = summa / len(chisla)
    minimum = min(chisla)
    maksimum = max(chisla)
    kolichestvo = len(chisla)
    
    # Возвращаем все результаты сразу
    return summa, srednee, minimum, maksimum, kolichestvo


def vyvod(summa, srednee, minimum, maksimum, kolichestvo):
    """Печатает результаты."""
    print("Количество:", kolichestvo)
    print("Сумма:", round(summa, 4))
    print("Среднее:", round(srednee, 4))
    print("Минимум:", minimum)
    print("Максимум:", maksimum)


# Запуск программы
chisla = vvod()
s, sr, mn, mx, kol = obrabotka(chisla)
vyvod(s, sr, mn, mx, kol)