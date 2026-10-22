# ===== ВЫЧИСЛЕНИЯ =====

def v_metry(ed, znachenie):
    """Переводит любую длину в метры."""
    if ed == "1":   # мм
        return znachenie / 1000
    if ed == "2":   # см
        return znachenie / 100
    if ed == "3":   # м
        return znachenie
    if ed == "4":   # км
        return znachenie * 1000
    if ed == "5":   # дюймы
        return znachenie * 0.0254
    return 0

def iz_metrov(ed, znachenie_v_metrah):
    """Переводит метры в нужную единицу."""
    if ed == "1":   # мм
        return znachenie_v_metrah * 1000
    if ed == "2":   # см
        return znachenie_v_metrah * 100
    if ed == "3":   # м
        return znachenie_v_metrah
    if ed == "4":   # км
        return znachenie_v_metrah / 1000
    if ed == "5":   # дюймы
        return znachenie_v_metrah / 0.0254
    return 0


# ===== ВВОД =====

def vvod():
    """Спрашивает единицы и число."""
    print("1 - мм, 2 - см, 3 - метры, 4 - км, 5 - дюймы")
    
    print("Из какой единицы переводим?")
    from_ed = input("Выбор: ")
    
    print("В какую единицу переводим?")
    to_ed = input("Выбор: ")
    
    try:
        znachenie = float(input("Введите значение: "))
    except ValueError:
        print("Ошибка: нужно ввести число.")
        return "0", "0", 0
        
    return from_ed, to_ed, znachenie


# ===== ВЫВОД =====

def vyvod(from_ed, to_ed, resultat):
    """Печатает результат перевода."""
    # Словарь для красивых названий
    nazvaniya = {
        "1": "мм",
        "2": "см",
        "3": "м",
        "4": "км",
        "5": "дюйм(ов)"
    }
    
    if from_ed == "0":
        return # Ошибка уже выведена
        
    print("Результат:", resultat, nazvaniya.get(to_ed, ""))


# ===== ГЛАВНАЯ ПРОГРАММА =====

f_ed, t_ed, znach = vvod()

if f_ed != "0":
    # Сначала переводим в базовые метры, потом в нужную единицу
    v_metrah = v_metry(f_ed, znach)
    itog = iz_metrov(t_ed, v_metrah)
    
    # Округляем, чтобы не было длинных дробей
    vyvod(f_ed, t_ed, round(itog, 4))