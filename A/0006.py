# Треугольник - 900
data = list(map(int, input().split()))

check_triangle = any((
    data[0] < data[1] + data[2] and data[1] < data[0] + data[2] and data[2] < data[0] + data[1],
    data[1] < data[2] + data[3] and data[2] < data[1] + data[3] and data[3] < data[1] + data[2],
    data[0] < data[2] + data[3] and data[2] < data[0] + data[3] and data[3] < data[0] + data[2],
    data[0] < data[1] + data[3] and data[1] < data[0] + data[3] and data[3] < data[0] + data[1]
))

check_segment = any((
    data[0] == data[1] + data[2] or data[1] == data[0] + data[2] or data[2] == data[0] + data[1],
    data[1] == data[2] + data[3] or data[2] == data[1] + data[3] or data[3] == data[1] + data[2],
    data[0] == data[2] + data[3] or data[2] == data[0] + data[3] or data[3] == data[0] + data[2],
    data[0] == data[1] + data[3] or data[1] == data[0] + data[3] or data[3] == data[0] + data[1]
))

print('TRIANGLE' if check_triangle else 'SEGMENT' if check_segment else 'IMPOSSIBLE')
