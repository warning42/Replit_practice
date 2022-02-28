n = int(input())
array1 = list(map(int, input().split()))

array1.sort()

m = int(input())
array2 = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return print('no', end=' ')
    mid = (start + end) // 2
    if array[mid] == target:
        return print('yes', end=' ')
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for i in range(m):
    binary_search(array1, array2[i], 0, n - 1)