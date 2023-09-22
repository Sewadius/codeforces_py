# Bit++ - 800
n = int(input())
result = 0
for _ in range(n):
    s = input()
    if '+' in s:
        result += 1
    else:
        result -= 1
print(result)
