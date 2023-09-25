# IQ тест - 1300
num_elements = int(input())
numbers = map(int, input().split())
parity_map = [bool(el % 2) for el in numbers]
print(parity_map.index(True) + 1 if sum(parity_map) == 1 else parity_map.index(False) + 1)
