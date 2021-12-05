import loaders

DAY = 0

def main():
	input_file = loaders.input_filename(DAY, use_example=True)
	text = loaders.get_text(input_file)
	print(text)

if __name__ == '__main__':
    main()