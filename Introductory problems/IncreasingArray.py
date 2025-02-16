n = int(input())
r = input()
cont = 0
num = [int(i)for i in r.split()]
num = num[0:n]
for i in range(1,n):
    if num[i] < num[i-1]:
        sum = num[i-1] - num[i]
        num[i] = num[i-1]
        cont += sum
print(cont)

