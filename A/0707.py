# Фотографии Брейна - 800
BLACK_WHITE = set('WGB')
colours = set()
for _ in range(list(map(int, input().split()))[0]):
    colours.update(input().split())
print('#Black&White' if colours.issubset(BLACK_WHITE) else '#Color')
