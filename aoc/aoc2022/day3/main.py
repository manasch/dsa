import string

alphabets = string.ascii_letters
with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]

def main():
    priority = 0
    for line in data:
        common = set(line[:len(line) // 2]).intersection(set(line[len(line) // 2:]))
        priority += alphabets.index(common.pop()) + 1
    
    print(priority)

def main2():
    priority = 0
    for i in range(0, len(data), 3):
        common = set(data[i]).intersection(set(data[i + 1]), set(data[i + 2]))
        priority += alphabets.index(common.pop()) + 1
    
    print(priority)

if __name__ == "__main__":
    main()
    main2()
