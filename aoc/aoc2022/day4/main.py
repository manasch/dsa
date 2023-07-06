with open("input.txt") as f:
    data = f.readlines()

def main():
    cnt = 0
    for line in data:
        sections = line.strip().split(',')
        l1, r1 = [int(x) for x in sections[0].split('-')]
        l2, r2 = [int(x) for x in sections[1].split('-')]
        
        if (l2 >= l1 and r2 <= r1) or (l1 >= l2 and r1 <= r2):
            cnt += 1
    
    print(cnt)

def main2():
    cnt = 0
    for line in data:
        sections = line.strip().split(',')
        l1, r1 = [int(x) for x in sections[0].split('-')]
        l2, r2 = [int(x) for x in sections[1].split('-')]

        if not (r1 < l2 or l1 > r2):
            cnt += 1
        
    print(cnt)
        

if __name__ == "__main__":
    main()
    main2()
