n = int(input())
num = []
while (n != 1):
    num.append(n)
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3
        n += 1

num.append(1)
print(*num)
