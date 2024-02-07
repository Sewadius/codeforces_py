# Слишком длинные слова - 800
n = int(input())
for _ in range(n):
    word, result = input(), ""
    result = word[0] + str(len(word) - 2) + word[-1] if len(word) > 10 else word
    print(result)
