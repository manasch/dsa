with open("input.txt") as f:
    data = f.read().split("\n\n")
    
    parts = data[0].split("\n")[:-1]
    stacks = [[] for _ in range(9)]

    for line in parts:
        crates = line[1::4]
        for i, crate in enumerate(crates):
            if crate != " ":
                stacks[i].append(crate)
    
    stacks = [stack[::-1] for stack in stacks]

    # for line in data[1].split("\n"):
    #     tokens = line.split()
    #     n, src, dst = map(int, [tokens[1], tokens[3], tokens[5]])
    #     src -= 1
    #     dst -= 1

    #     for i in range(n):
    #         stacks[dst].append(stacks[src].pop())
    
    # for i in range(9):
    #     print(stacks[i][-1], end="")
    

    for line in data[1].split("\n"):
        tokens = line.split()
        n, src, dst = map(int, [tokens[1], tokens[3], tokens[5]])
        src -= 1
        dst -= 1

        temp = []
        for i in range(n):
            temp.append(stacks[src].pop())
        stacks[dst].extend(temp[::-1])
    
    for i in range(9):
        print(stacks[i][-1], end="")
