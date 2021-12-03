def part1(list: list):
    increase = 0    
    
    for count, i in enumerate(list):
        if count > 0 and int(i) > int(list[count-1]):
           increase += 1  
           
    return increase

def part2(list: list):
    listofsums = []
    
    for count, i in enumerate(list):
        if count >= 2:
            listofsums.append(int(i) + int(list[count-1]) + int(list[count-2]))

    increased = [i for count, i in enumerate(listofsums) if i > listofsums[count-1] and count > 0]
    return len(increased)

if __name__ == '__main__':
    with open("Day1_input.txt", "r") as f:
        data = f.read()

    list = data.split('\n')

    print(f'Part 1: {part1(list)}\nPart 2: {part2(list)}')