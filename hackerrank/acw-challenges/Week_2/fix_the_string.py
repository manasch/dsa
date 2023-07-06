n = input()
string = input().rstrip()

left = string.count('(')
right = string.count(')')

if left != right:
    print(-1)
else:
    stack = []

    for index in range(n):
        if string(index) == '(':
            stack.append(index)