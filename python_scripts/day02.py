import loaders

DAY = 2

class Submarine:
    def __init__(self):
        self.depth = 0
        self.x_coord = 0
        self.aim = 0
    
    def move_directly(self, dir, amount):
        if dir == "forward":
            self.x_coord += amount
        elif dir == "up":
            self.depth -= amount
        else:
            self.depth += amount


    def move_with_aim(self, dir, amount):
        if dir == "forward":
            self.x_coord += amount
            self.depth += self.aim * amount
        elif dir == "up":
            self.aim -= amount
        else:
            self.aim += amount


def main():
    input_file = loaders.input_filename(DAY, use_example=False)
    pattern = '(?P<dir>\w+) (?P<amt>\d+)'
    instructs = loaders.get_dict_iter(input_file, pattern)
    sub = Submarine()
    for inst in instructs:
        dir, amt = inst["dir"], int(inst["amt"])
        sub.move_with_aim(dir, amt)
    print(sub.x_coord * sub.depth)

if __name__ == '__main__':
    main()