# Шипы и монеты
for _ in range(int(input())):
    input()
    spike = (line := input()).find('**')
    coins = line.count('@') if spike == -1 else line[:spike].count('@')
    print(coins)
