# Петя и строки - 800
s1, s2 = [input().lower() for _ in range(2)]
print('-1' if s1 < s2 else '1' if s2 < s1 else '0')
