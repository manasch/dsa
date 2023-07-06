def main():
    with open("input.txt") as f:
        data = f.readlines()
    
    calories = []
    cal_sum = 0
    for line in data:
        if line == '\n':
            calories.append(cal_sum)
            cal_sum = 0
            continue
        
        cal_sum += int(line.strip())
    
    print(max(calories))

def main2():
    with open("input.txt") as f:
        data = f.readlines()
    
    calories = []
    cal_sum = 0
    for line in data:
        if line == '\n':
            calories.append(cal_sum)
            cal_sum = 0
            continue
        
        cal_sum += int(line.strip())
    
    print(sum(sorted(calories, reverse=True)[:3]))

if __name__ == "__main__":
    main()
    main2()
