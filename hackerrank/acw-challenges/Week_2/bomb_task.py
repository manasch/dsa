n = int(input())
string = input().rstrip()

flag = 1
sub = 'AB'
count = 0

while flag:
    count += 1
    if sub in string:
        i = string.index(sub)
        string = string[:i] + string[i+2:]
    else:
        flag = 0

if count:
    print(len(string))
else:
    print(0)