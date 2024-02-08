# Слово - 800
word, counter = input(), 0
for ch in word:
    if ch == ch.upper():
        counter += 1
print(word.upper() if counter > len(word) / 2 else word.lower())
