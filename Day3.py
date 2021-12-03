from statistics import mode

with open("Day3_input.txt", "r") as f:
    data = f.read()
    
matrix = [[], [], [], [], [], [], [], [], [], [], [], []]

for x in data.split("\n"):
    for i, j in enumerate(x):
        matrix[i].append(j)
    
frequency = [mode(matrix[i]) for i, _ in enumerate(matrix)]
gamma_rate, epsilon_rate = "", ""

for i in frequency:
    gamma_rate += i
    if i  == "0":
        epsilon_rate += "1"
    else: epsilon_rate += "0"

print(int(gamma_rate, 2)*int(epsilon_rate, 2))