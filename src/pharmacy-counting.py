from os.path import join, dirname, abspath
from operator import itemgetter

data_folder = join(dirname(dirname(abspath(__file__))), "input")

file_to_open = join(data_folder, "icont.txt")


drug_providers = {}

total_cost = {}


def listify_line(line):
    return line.split(",")

with open(file_to_open) as f:
    next(f)
    for line in f:
        line = line.strip()
        line = listify_line(line)
        provider = line[1] + " " + line[2]
        drug = line[3]
        cost = int(line[4])
        if drug not in drug_providers:
            drug_providers[drug] = set([provider])
            total_cost[drug] = cost
        else:
            drug_providers[drug].add(provider)
            total_cost[drug] += cost

drug_cost_total = []

for drug, total_cost in total_cost.items():
    drug_cost_total.append((total_cost, drug))

drug_cost_total.sort(key=lambda x: x[0], reverse=True)

print(drug_cost_total)


# output_data_folder = join(dirname(dirname(abspath(__file__))), "output")

# with open(join(output_data_folder, 'top_drug_cost.txt'), 'w') as drug_cost:
#     for drug in drug_providers:
#         total_providers = str(len(drug_providers[drug]))
#         drug_cost.write(drug + "," + total_providers + "," + str(total_cost[drug]) + "\n")
