# n = int(input())

# def find_sum(numlen, arr):
#     for i in range(numlen):
        


# for _ in range(n):
#     numlen = input()
#     arr = [int(i) for i in input().split()]
#     ans = find_sum(numlen, arr)

num = 20
rem = -1
count = 0
while rem != 0:
    start = 2
    while start * 2 <= num and rem:
        start *= 2
        count += 1
        rem = num - start
        print(start, 't')
    num = rem
    print(rem, 'p', count)
    count = 0