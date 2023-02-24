def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


Pos = [10, 29, 18, 17, 0, 2]
bubbleSort(Pos)

print('Отсортированные числа:')
print(Pos)

def binary_search(A, Val):
    N = len(A)
    ResultOk = False
    First = 0
    Last = N - 1

    while First <= Last:
        Middle = (First + Last) // 2
        if A[Middle] == Val:
            ResultOk = True
            Pos = Middle
            break
        elif A[Middle] > Val:
            Last = Middle - 1
        else:
            First = Middle + 1

    if ResultOk:
        print(f"Число {Val} найден\nПод индексом:")
        print(Pos)
    else:
        print(f"Число {Val} не найдено")

Val = 29
binary_search(Pos, Val)













