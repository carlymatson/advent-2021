import re
import pathlib

import loaders

p = pathlib.Path('.')
INPUT_FILE = p.parent / "inputs/sample_input.txt"
PATTERN = "(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pwd>\w+)"
PATTERN2 = "(?P<color1>[a-z ]+) bags contain (?P<contents>[0-9a-z, ]+)\."

def check_square(grid, x, y, character):
    return

def count_adjacent(grid, position, character, include_center = False) -> int:
    x, y = position
    top, bottom = 0, len(grid)
    left, right = 0, len(grid[y])
    for y2 in [y-1, y, y+1]:
        for x2 in [x-1, x, x+1]:
            check_square(grid, x2, y2, character)
    return 0

def is_valid(min, max, char, pwd):
    count = pwd.count(char)
    if int(min) <= count and count <= int(max):
        return True
    return False

def main():
    rules = loaders.get_dict_iter(INPUT_FILE, PATTERN2)
    for r in rules:
        print(r)

if __name__ == '__main__':
    main()