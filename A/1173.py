# Nauuo и голоса - 800
plus, minus, unknown = [int(i) for i in input().split()]
delta = max(plus, minus) - min(plus, minus)

if plus == minus and unknown == 0:
    print('0')
elif delta > unknown:
    print('+' if plus > minus else '-')
else:
    print('?')
