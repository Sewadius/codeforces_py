# Сделайте белой
for _ in range(int(input())):
    input()
    line = input()
    print(line.rfind('B') - line.find('B') + 1)
