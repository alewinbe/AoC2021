from statistics import mode

def part1(data: list):
    matrix = create_matrix(data)    
    frequency = most_frequent_bit(matrix)
    gamma_rate, epsilon_rate = "", ""

    for i in frequency:
        gamma_rate += i
        if i  == "0":
            epsilon_rate += "1"
        else: epsilon_rate += "0"
        
    return int(gamma_rate, 2)*int(epsilon_rate, 2)

def create_matrix(data: list):
    matrix = [[], [], [], [], [], [], [], [], [], [], [], []]

    for x in data:
        for i, j in enumerate(x):
            matrix[i].append(j)
    return matrix

def most_frequent_bit(matrix: list):
    return [mode(matrix[i]) for i, _ in enumerate(matrix)]

def part2(data: list):
    matrix = create_matrix(data)    
    frequency = most_frequent_bit(matrix)
    oxygen_rating, c02_rating = data[:], data[:]
    
    for i in range(12):
        for j in data:
            if len(oxygen_rating) > 1 and j[i] != frequency[i] and j in oxygen_rating:
                oxygen_rating.remove(j)
            if len(c02_rating) > 1 and j[i] == frequency[i] and j in c02_rating:
                c02_rating.remove(j)
                
    return int(oxygen_rating[0], 2)*int(c02_rating[0], 2)
    
    
if __name__ == "__main__":
    with open("Day3_input.txt", "r") as f:
        data = f.read()
        data = data.split("\n")
        
    print(f'Part 1: {part1(data)}\nPart 2: {part2(data)}')