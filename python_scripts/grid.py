
class Grid:
    UP = (0,1)
    DOWN = (0,-1)
    LEFT = (-1,0)
    RIGHT = (1,0)
    CARDINALS = {'U': (1,0), 'D': (-1,0), 'L': (-1,0), 'R': (-1,0)}
    DIAGONALS = {'UR': (1,1), 'DR': (1,1), 'UL': (1,1), 'DL': (1,1)}

    def __init__(self, grid):
        self.grid = grid
        self.x_min = 0
        self.x_max = len(grid[0]) - 1
        self.y_min = 0
        self.y_may = len(grid) - 1

    @classmethod
    def from_string(cls, text, row_splitter='\n', col_splitter=',', row_parser=None):
        if row_parser is None:
            row_parser = lambda s: s.split(col_splitter) # Use regex instead?
        rows = text.split(row_splitter)
        grid = [row_parser(row) for row in rows]
        return grid

    def add(pt1, pt2):
        return (pt1[0] + pt2[0], pt1[1] + pt2[1])

    def is_valid(self, x, y):
        valid_x = (self.x_min <= x) and (x <= self.x_max)
        valid_y = (self.y_min <= y) and (y <= self.y_may)
        return valid_x and valid_y

    def get_connections(self, x, y, include_diagonals = False):
        moves = Grid.CARDINALS
        if include_diagonals:
            moves = moves + Grid.DIAGONALS
        connections = []
        for vector in moves:
            point_b = Grid.add((x,y), vector)
            if self.is_valid(point_b):
                connections.append(point_b)
        return connections

    def print_grid(self, formatter=None, joiner=' ', icon_width=1):
        for row in self.grid:
            if formatter is None:
                formatter = lambda x: f'{x:{icon_width}}'
            formatted_entries = [formatter(x) for x in row]
            print(joiner.join(formatted_entries))