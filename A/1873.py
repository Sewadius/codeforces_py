# Короткая сортировка
n = int(input())
data = [input() for _ in range(n)]
for el in data:
    print('YES' if el in ('abc', 'cba', 'acb', 'bac') else 'NO')
