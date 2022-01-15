from typing import Tuple, Protocol
from dataclasses import dataclass
from colored import fore, style


class PrintableGrid(Protocol):
    def get_icon(x: int, y: int) -> str:
        pass

    def get_bounds(axis: str) -> Tuple[int, int]:
        pass


def print_grid(g: PrintableGrid):
    for y in range(*g.get_bounds("y")):
        icons = [g.get_icon((x, y)) for x in range(*g.get_bounds("x"))]
        print("".join(icons))


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"


def game_loop():
    response = ""
    while response != "quit":
        print("Pew!")
        response = input()
        print(response)


def highlight(text, styles=None):
    if styles is None:
        styler = fore.RED + style.BOLD
    else:
        styler = ""
        for s in styles:
            styler += s
    return styler + text + style.RESET


def colorize():
    print("Hi " + highlight("Carly", fore.GREEN) + "!")


colorize()
