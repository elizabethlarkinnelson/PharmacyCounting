from os.path import join, dirname, abspath

data_folder = join(dirname(dirname(abspath(__file__))), "input")

file_to_open = join(data_folder, "icont.txt")


drugs = {}


def listify_line(line):
    return line.split(",")

with open(file_to_open) as f:
    next(f)
    for line in f:
        line = line.strip()
        line = listify_line(line)
        provider = line[1] + " " + line[2]
        drug = (line[3], line[4])
        if drug not in drugs:
            drugs[drug] = set([provider])
        else:
            #set.add() doesn't add to set if already there
            drugs[drug].add(provider)

print(drugs)
