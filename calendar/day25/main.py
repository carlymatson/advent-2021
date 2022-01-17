from pathlib import Path


def load_input(example=None):
    file_name = "input.txt" if example is None else f"example{example}.txt"
    path = Path(__file__).parent / file_name
    text = path.read_text()
    grid = text.split("\n")
    print(len(grid), len(grid[0]))
    return grid


def make_wrapped_point_class(width, height):
    class WrappedPoint:
        def __init__(self, x, y):
            self.x = x % width
            self.y = y % height

        def __eq__(self, other):
            return (self.x == other.x) and (self.y == other.y)

        def __add__(self, other):
            return WrappedPoint(self.x + other.x, self.y + other.y)

        def __hash__(self):
            return hash((self.x, self.y))

        def __repr__(self):
            return f"({self.x}, {self.y})"

    return WrappedPoint


# Use dimensions of grid to create WrapPoint (hash tuple)
class Seafloor:
    def __init__(self, rows):
        self.width = len(rows[0])
        self.height = len(rows)
        self.WrapPoint = make_wrapped_point_class(self.width, self.height)
        self.south_herd = Seafloor.find_herd(rows, "v", self.WrapPoint)
        self.east_herd = Seafloor.find_herd(rows, ">", self.WrapPoint)

    @staticmethod
    def find_herd(rows, symbol, point_constructor):
        return set(
            [
                point_constructor(x, y)
                for x in range(len(rows[0]))
                for y in range(len(rows))
                if rows[y][x] == symbol
            ]
        )

    def is_occupied(self, point):
        if point in self.south_herd:
            return True
        if point in self.east_herd:
            return True
        return False

    def get_icon(self, x, y):
        if self.WrapPoint(x, y) in self.south_herd:
            return "v"
        if self.WrapPoint(x, y) in self.east_herd:
            return ">"
        return "."

    def get_bounds(self, axis):
        if axis == "x":
            return 0, self.width
        if axis == "y":
            return 0, self.height

    def move_herd(self):  # FIXME Point addition won't work, so this won't work
        # East
        dir = self.WrapPoint(1, 0)
        new_locs = set(
            [
                point + dir if not self.is_occupied(point + dir) else point
                for point in self.east_herd
            ]
        )
        self.east_herd = new_locs
        # South
        dir = self.WrapPoint(0, 1)
        new_locs = set(
            [
                point + dir if not self.is_occupied(point + dir) else point
                for point in self.south_herd
            ]
        )
        self.south_herd = new_locs

    def __repr__(self):
        icons = [
            [self.get_icon(x, y) for x in range(self.width)] for y in range(self.height)
        ]
        return "\n".join(["".join(row) for row in icons])


def main():
    input = load_input(example=None)
    sf = Seafloor(input)
    prev_state = ""
    turns = 0
    while str(sf) != prev_state:
        if False:
            print(f"After {turns} steps:")
            print(sf)
            print("")
        prev_state = str(sf)
        sf.move_herd()
        turns += 1
        if turns % 10 == 0:
            print(".")
        if turns > 1000:
            print("AAAAAH!")
            break
    print(sf)
    print(turns)


if __name__ == "__main__":
    main()
