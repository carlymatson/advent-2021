from collections import Counter, defaultdict
import loaders

DAY = 14


def grow_polymer(polymer, rules):
    new_polymer = polymer[0]
    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        middle = rules[pair]
        new_polymer += middle + pair[1]
    return new_polymer


def add_to_count(counts, item, number):
    if item not in counts:
        counts[item] = 0
    counts[item] += number
    return counts


def polymer_to_pair_counts(polymer):
    poly_pairs = [polymer[i : i + 2] for i in range(len(polymer) - 1)]
    poly_counts = Counter(poly_pairs)
    return poly_counts


def grow_pair_counts(poly_count, rules):
    for pair, count in list(poly_count.items()):
        insert = rules[pair]
        pair1 = pair[0] + insert
        pair2 = insert + pair[1]
        poly_count = add_to_count(poly_count, pair, -count)
        poly_count = add_to_count(poly_count, pair1, count)
        poly_count = add_to_count(poly_count, pair2, count)
    return poly_count


def pair_to_char_counts(poly_counts, first, last):
    """Total the number of times each character appears in a pair and divide by 2."""
    char_counts = {}
    for pair, count in poly_counts.items():
        a, b = pair
        add_to_count(char_counts, a, count)
        add_to_count(char_counts, b, count)
    # The first and last characters are the only ones not double-counted.
    char_counts[first] += 1
    char_counts[last] += 1
    char_counts = {char: int(count / 2) for char, count in char_counts.items()}
    return char_counts


def main():
    # Load input - get starting polymer and substitution rules
    input_file = loaders.input_filename(DAY, use_example=False)
    text = loaders.get_text(input_file)
    lines = text.split("\n")
    polymer = lines[0]
    pattern = "(?P<pair>\w+) -> (?P<res>\w+)"
    rules = loaders.get_dict_iter(input_file, pattern)
    subs = {rule["pair"]: rule["res"] for rule in rules}

    pair_count = polymer_to_pair_counts(polymer)
    for step in range(40):
        pair_count = grow_pair_counts(pair_count, subs)
        # polymer = grow_polymer(polymer, subs)
        if step % 5 == 0:
            print(f"Step {step}...")
    ### Part 1 ###
    # char_counts = Counter(polymer)
    ### Part 2 ###
    first_char = polymer[0]
    last_char = polymer[-1]
    char_counts = pair_to_char_counts(pair_count, first_char, last_char)

    # Get difference between minimum and maximum character counts.
    counts = char_counts.values()
    diff = max(counts) - min(counts)
    print(f"Difference: {diff}")


if __name__ == "__main__":
    main()
