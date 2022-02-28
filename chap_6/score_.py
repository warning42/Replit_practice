n = int(input())

a = []

for i in range(n):
    array = input().split()
    a.append((array[0], int(array[1])))

def sort_key(data):
    return data[0]

a.sort(key=sort_key)
             
for i in range(n):
    print(a[i][0], end=' ')