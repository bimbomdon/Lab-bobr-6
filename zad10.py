import datetime

def visokosnyy(god):
    """Проверяет, является ли год високосным."""
    # Год високосный, если делится на 4, но не на 100, либо делится на 400
    if (god % 4 == 0 and god % 100 != 0) or (god % 400 == 0):
        return True
    return False


def raznost_dat(d1, d2):
    """Считает разницу в днях между двумя датами."""
    # Вычитаем одну дату из другой и берём модуль (чтобы не было минуса)
    delta = abs((d2 - d1).days)
    return delta


def den_nedeli(d):
    """Возвращает день недели для даты."""
    # Словарь для перевода номера дня недели в русское название
    dni = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье"
    }
    # d.weekday() возвращает число от 0 (Пн) до 6 (Вс)
    return dni[d.weekday()]

def vvod():
    """Спрашивает, что нужно сделать, и запрашивает данные."""
    print("1 - Проверить год на високосность")
    print("2 - Разность двух дат")
    print("3 - Узнать день недели")
    vibor = input("Выбор: ")

    if vibor == "1":
        god = int(input("Введите год: "))
        return "1", god

    if vibor == "2":
        print("Введите первую дату (например, 2023-10-05):")
        d1 = datetime.datetime.strptime(input(), "%Y-%m-%d").date()
        print("Введите вторую дату:")
        d2 = datetime.datetime.strptime(input(), "%Y-%m-%d").date()
        return "2", (d1, d2)

    if vibor == "3":
        print("Введите дату (например, 2023-10-05):")
        d = datetime.datetime.strptime(input(), "%Y-%m-%d").date()
        return "3", d

    return "0", None

def vyvod(vibor, rezultat):
    """Печатает результат в зависимости от выбора."""
    if vibor == "1":
        if rezultat:
            print("Год високосный.")
        else:
            print("Год НЕ високосный.")
    elif vibor == "2":
        print("Разница между датами:", rezultat, "дней.")
    elif vibor == "3":
        print("День недели:", rezultat)

vibor, dannye = vvod()

if vibor == "1":
    vyvod(vibor, visokosnyy(dannye))
elif vibor == "2":
    vyvod(vibor, raznost_dat(dannye[0], dannye[1]))
elif vibor == "3":
    vyvod(vibor, den_nedeli(dannye))
else:
    print("Неверный пункт меню.")