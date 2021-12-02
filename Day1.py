with open("Day1_commands.txt", "r") as f:
    data = f.read()

list = data.split('\n')
# increase = 0

# for count, i in enumerate(list):
#     if count > 0 and int(i) > int(list[count-1]):
#        increase += 1 
       
# print(increase)

listofsums = []

for count, i in enumerate(list):
    if count >= 2:
        listofsums.append(int(i) + int(list[count-1]) + int(list[count-2]))

increased = [i for count, i in enumerate(listofsums) if i > listofsums[count-1] and count > 0]
print(len(increased))