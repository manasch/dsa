n, q = input().split()
array = [int(i) for i in input().split()]

def binary_search(array, start, end, key):
    if end >= start:
        mid = int(start + (end - start) / 2)
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            binary_search(array, mid + 1, end, key)
        else:
            binary_search(array, start, mid - 1, key)
    else:
        return -1

for _ in range(int(q)):
    key = int(input())
    res = binary_search(array, 0, len(array) - 1, key)
    if res < 0:
        print('NO')
    else:
        print('YES')