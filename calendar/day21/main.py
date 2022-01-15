def die_roll():
    roll = 1
    while True:
        yield roll
        roll += 1


class Player:
    def __init__(self, starting_space, die_roll):
        self.space = starting_space
        self.score = 0
        self.die_roll = die_roll

    def move(self, num_spaces):
        self.space += num_spaces % 10
        if self.space > 10:
            self.space -= 10

    def take_turn(self):
        # print(f"Player rolls...")
        for _ in range(3):
            roll = next(self.die_roll)
            # print(roll)
            self.move(roll)
        self.score += self.space
        # print(f"...for a score of {self.score}")

    def __repr__(self):
        return f"P(x={self.space},score={self.score})"


def main():
    die = die_roll()
    p1 = Player(7, die)
    p2 = Player(6, die)
    turns = 0
    while turns > -1:
        turns += 1
        p1.take_turn()
        if p1.score >= 1000:
            other_score = p2.score
            break
        p2.take_turn()
        if p2.score >= 1000:
            other_score = p1.score
            break
    print(p1, p2)
    next_roll = next(die)
    answer = other_score * (next_roll - 1)
    print(f"Score: {next_roll-1} * {other_score} = {answer}")


if __name__ == "__main__":
    main()
