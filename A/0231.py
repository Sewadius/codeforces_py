# Команда - 800
counter = 0
for _ in range(int(input())):
    lst = list(map(int, input().split()))
    if lst.count(1) >= 2:
        counter += 1
print(counter)
