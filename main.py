from random import randint
N = 10
a = [randint(1, 10) for i in range(N)]
print(a)

for i in range(N-1):
    for j in range(N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1
x = 9
index = binary_search(a, x)

if index != -1:
    print(f"Нашел {x} под индексом {index}")
else:
    print(f"{x} не удалось найти")




