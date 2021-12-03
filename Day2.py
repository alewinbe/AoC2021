class Submarine:
    def __init__(self):
        self.depth = 0
        self.horizontal_position = 0
        self.aim = 0
    
    def __str__(self):
        return f'Depth: {self.depth}\nHorizontal position: {self.horizontal_position}\nAim: {self.aim}\nMultiplied: {self.multiply()}'

    def up(self, amount: int):
        self.aim -= amount

    def down(self, amount: int):
        self.aim += amount

    def forward(self, amount: int):
        self.horizontal_position += amount
        self.depth += self.aim * amount

    def multiply(self):
        return self.horizontal_position*self.depth


if __name__ == '__main__':
    sub = Submarine()
    with open("Day2_input.txt", "r") as f:
        data = f.read()
       
    for x in data.split("\n"):
        if "forward" in x:
            sub.forward(int(x[8:]))
        elif "up" in x:
            sub.up(int(x[3:]))
        elif "down" in x:
            sub.down(int(x[5:]))
       
    print(sub)