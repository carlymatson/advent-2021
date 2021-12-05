import loaders

DAY = 1

def main():
    INPUT_FILE = loaders.input_filename(DAY, use_example=False)
    numbers = loaders.get_int_list(INPUT_FILE)
    sums = [numbers[i] + numbers[i+1] + numbers[i+2] for i in range(len(numbers) - 2)]
    numbers = sums
    increase_count = 0
    prev = numbers[0]
    for num in numbers[1:]:
        if num > prev:
            increase_count += 1
        prev = num
    print(f'Number of increases: {increase_count}')

if __name__ == '__main__':
    main()