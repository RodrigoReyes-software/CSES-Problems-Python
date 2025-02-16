
cont = 1
r = 0
word = input()
for i in range(len(word)-1):
    if word[i] == word[i+1]:
        cont+=1
    else:
        if cont > r:
            r = cont
        cont = 1
if cont > r: r = cont
print(r)
