# Два сосуда
number_inputs = int(input())
data = [list(map(int, input().split())) for _ in range(number_inputs)]
results = []
for el in data:
    if el[0] == el[1]:
        results.append(0)
        continue
    counter = 0
    mean = (el[0] + el[1]) / 2
    min_element = min(el[0], el[1])
    while min_element < mean:
        min_element += el[2]
        counter += 1
    results.append(counter)
print(*results, sep='\n')
