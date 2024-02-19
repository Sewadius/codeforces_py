# Халк - 800
s = "I hate"
for i in range(1, int(input())):
    s = f'{s} that I love' if i % 2 else f'{s} that I hate'
print(f'{s} it')
