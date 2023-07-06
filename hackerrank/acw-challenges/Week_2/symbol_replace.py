n = int(input())

def get_eaten(path, food):
    eaten = ''
    last = ''
    for char in food:
        if char.islower():
            eaten += char
            last += char
            if char not in eaten[-2:]:
                last = last[:-1]
        elif last and char == '#':
            eaten += last[-1]
        elif last and char == '-':
            last = last[:-1]
        else:
            continue

    return eaten

for i in range(n):
    path = int(input())
    food = input()

    eaten = get_eaten(path, food)

    print(eaten)
