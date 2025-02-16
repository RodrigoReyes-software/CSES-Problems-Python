n = int(input())
num = []
if n == 2 or n == 3:
    print("NO SOLUTION")
else:
    for i in range(2, n + 1, 2):
        num.append(i)
    for i in range(1, n + 1, 2):
        num.append(i)
        i += 1
print(*num)

