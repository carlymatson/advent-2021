import pathlib

import loaders

p = pathlib.Path('.')
INPUT_FILE = p.parent / "inputs/day01.txt"

def main():
	text = loaders.get_text(INPUT_FILE)
	print(text)

if __name__ == '__main__':
    main()