from os.path import join, dirname, abspath

data_folder = join(dirname(dirname(abspath(__file__))), "input")

file_to_open = join(data_folder, "icont.txt")

f = open(file_to_open)

