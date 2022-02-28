n = int(input())

m = []

for i in range(n):
    m.append(int(input()))

m.sort(reverse=True)
for i in range(n):
    print(m[i], end=' ')