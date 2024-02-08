# HQ+ - 900
word, check = input(), ('H', 'Q', '9')
for ch in check:
    if ch in word:
        print('YES')
        break
else:
    print('NO')
