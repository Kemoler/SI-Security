def calculate(m: int, n: int, p: list[int]):
    if m == -1:  # Акция закончилась
        return 0
    if n == len(p):  # Акция началась
        return calculate(m - 1, 0, p)
    if n == len(p) - 1:  # Получили все n наград
        return calculate(m - 1, 0, p) + p[n]
    return max(calculate(m - 1, 0, p),
               calculate(m - 1, n + 1, p) + p[n])  # Пропускаем день или получаем его вознаграждение


print(calculate(3, 3, [6, 2, 3]))  # 12
print(calculate(3, 3, [2, 4, 8]))  # 14
print(calculate(6, 6, [10, 1, 1, 1, 1, 18]))  # 32
print(calculate(6, 6, [10, 1, 1, 1, 1, 17]))  # 31
print(calculate(1, 3, [6, 2, 3]))  # 6
print(calculate(0, 3, [6, 2, 3]))  # 0
print(calculate(3, 1, [6]))  # 18
