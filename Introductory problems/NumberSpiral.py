t = int(input())  # Lee el número de pruebas

for i in range(t):
    x, y = map(int, input().split())
    if x > y:
        if x % 2 == 0:
            result = x ** 2 - (y - 1)
        else:
            result = x ** 2 - (2 * x - 1) + y
    else:
        if y % 2 == 0:
            result = y ** 2 - (2 * y - 1) + x
        else:
            result = y ** 2 - (x - 1)
    print(result)
