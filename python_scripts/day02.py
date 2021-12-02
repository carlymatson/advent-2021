import pathlib

import loaders

p = pathlib.Path('.')
INPUT_FILE = p.parent / "inputs/day02.txt"
PATTERN = "(?P<dir>\w+) (?P<amt>\d+)"

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
    instructs = loaders.get_dict_iter(INPUT_FILE, PATTERN)
    sub = Submarine()
    for inst in instructs:
        dir, amt = inst["dir"], int(inst["amt"])
        sub.move_with_aim(dir, amt)
    print(sub.x_coord * sub.depth)

if __name__ == '__main__':
    main()