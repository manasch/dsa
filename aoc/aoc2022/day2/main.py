def main():
    with open("input.txt") as f:
        data = f.readlines()
    
    total = 0
    prize = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    '''
    Convert
    X -> A
    Y -> B
    Z -> C

    if you win, difference is either 1 or -2

    '''
    
    for line in data:
        moves = line.strip().split()
        D = (ord(moves[1]) - 23) - ord(moves[0])
        if D == 0:
            result = 3
        elif D == 1 or D == -2:
            result = 6
        else:
            result = 0
        
        total += result + prize[moves[1]]
    
    print(total)

def main2():
    with open("input.txt") as f:
        data = f.readlines()
    
    total = 0
    result = {
        'X': -1,
        'Y': 0,
        'Z': 1
    }
    prize = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    '''
    To win, difference should be 1, loop around at when 2 + 1 > 3 there for mod 3
    To lose, difference should be -1
    '''

    choices = ['A', 'B', 'C']
    for line in data:
        moves = line.strip().split()
        if result[moves[1]] == 1:
            k = (choices.index(moves[0]) + 1) % 3
            total += (6 + prize[choices[k]])
        elif result[moves[1]] == 0:
            total += (3 + prize[moves[0]])
        else:
            k = choices.index(moves[0]) - 1
            total += prize[choices[k]]
    
    print(total)

if __name__ == "__main__":
    main()
    main2()