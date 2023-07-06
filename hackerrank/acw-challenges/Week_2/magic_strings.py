n = int(input())

def get_ans(exp):
    stack = []

    for char in exp:
        if char in ['(', '[', '{']:
            stack.append(char)
        
        else:
            # stack is empty
            if not stack:
                return 0
            cur = stack.pop()

            if cur == ')':
                if char != '(':
                    return 0
            if cur == ']':
                if char != '[':
                    return 0
            if cur == '}':
                if char != '{':
                    return 0
    
    if stack:
        return 0
    return 1

for i in range(n):
    exp = input().rstrip()
    ans = get_ans(exp)

    if ans:
        print('YES')
    else:
        print('NO')