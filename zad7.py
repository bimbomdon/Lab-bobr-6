def sortirovka_puzyrkom(spisok):
    """Пузырьковая сортировка: сравниваем соседние элементы и меняем их местами."""
    a = spisok.copy()  # копия, чтобы не портить исходный
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                # Меняем местами
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def sortirovka_vyborom(spisok):
    """Сортировка выбором: ищем минимум и ставим его в начало."""
    a = spisok.copy()
    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        # Меняем текущий элемент с найденным минимумом
        a[i], a[min_index] = a[min_index], a[i]
    return a


def proverka_uporyadochennosti(spisok):
    """Проверяет, отсортирован ли список по возрастанию."""
    for i in range(len(spisok) - 1):
        if spisok[i] > spisok[i + 1]:
            return False
    return True

def vvod():
    """Спрашивает числа для сортировки и выбор алгоритма."""
    print("Введите числа через пробел:")
    s = input()
    try:
        # Собираем числа в список
        chisla = [float(x) for x in s.split()]
    except ValueError:
        print("Ошибка: нужно вводить числа.")
        return None, "0"

    print("1 - Пузырьковая сортировка")
    print("2 - Сортировка выбором")
    vibor = input("Выберите алгоритм: ")
    
    return chisla, vibor

def vyvod(ischodnye, otvet, uporyadochen):
    """Печатает результат."""
    print("Исходный список:", ischodnye)
    print("Отсортированный список:", otvet)
    if uporyadochen:
        print("Проверка: список упорядочен.")
    else:
        print("Проверка: список НЕ упорядочен (ошибка алгоритма).")


chisla, vibor = vvod()

if chisla is not None:
    if vibor == "1":
        rezultat = sortirovka_puzyrkom(chisla)
        vyvod(chisla, rezultat, proverka_uporyadochennosti(rezultat))
    elif vibor == "2":
        rezultat = sortirovka_vyborom(chisla)
        vyvod(chisla, rezultat, proverka_uporyadochennosti(rezultat))
    else:
        print("Неверный выбор алгоритма.")