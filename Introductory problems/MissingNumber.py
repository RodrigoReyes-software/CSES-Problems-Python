n = int(input())
numeros = list(map(int, input().split()))
suma_total = n * (n + 1) // 2
suma_actual = sum(numeros)
faltante = suma_total - suma_actual
print(faltante)