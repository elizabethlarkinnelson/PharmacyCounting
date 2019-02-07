from os.path import join, dirname, abspath


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

output_data_folder = join(dirname(dirname(abspath(__file__))), "output")


with open(join(output_data_folder, 'top_drug_cost.txt'), 'w') as drug_cost:
    drug_cost.write('drug_name,num_prescriber,total_cost\n')
    for item in drug_cost_total:
        drug_name = item[1]
        cost_of_drug = item[0]
        providers_total = len(drug_providers[drug_name])
        drug_cost.write(drug_name + "," + str(providers_total) + "," + str(cost_of_drug) + "\n")
