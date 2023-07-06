n = int(input())

def find_harry(n, matrix):
    harry = -1
    other = []
    for i in range(n):
        if 1 not in matrix[i]: # i doesn't know anyone, could be harry
            for x, j in enumerate(matrix):
                if i != x:
                    other.append(j[i])
            if 0 not in other: # other contains the list of people who might or might not know
                harry = i + 1
                break
            else:
                other = []

    return harry


for _ in range(n):
    size = int(input())
    array = []
    for i in range(size):
        array.append([int(i) for i in input().strip().split()])
    person = find_harry(size, array)

    print(person)
