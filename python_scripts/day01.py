import pathlib

import loaders

p = pathlib.Path('.')
INPUT_FILE = p.parent / "inputs/day01.txt"#_example.txt"

def main():
	#text = loaders.get_text(INPUT_FILE)
	nums = loaders.get_int_list(INPUT_FILE)
	sums = [nums[i] + nums[i+1] + nums[i+2] for i in range(len(nums) - 2)]
	nums = sums
	print(nums)
	increase_count = 0
	prev = nums[0]
	for num in nums[1:]:
		if num > prev:
			increase_count += 1
		prev = num
	print(increase_count)

if __name__ == '__main__':
    main()