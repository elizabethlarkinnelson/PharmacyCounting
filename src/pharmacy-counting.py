from os.path import join, dirname, abspath

data_folder = join(dirname(dirname(abspath(__file__))), "input")

file_to_open = join(data_folder, "icont.txt")


drugs = {}

with open(file_to_open) as f:
	next(f)
	for line in f:
		line = line.strip()
		print(line)