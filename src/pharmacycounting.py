from os.path import join, dirname, abspath
import sys

test = 'hi'


#Getting filepath of input file named 'icont.txt'
data_folder = join(dirname(dirname(abspath(__file__))), "input")
file_to_open = join(data_folder, "icont.txt")

#drug_providers stores drug name key to set of provider names. Example - 'AMBIEN' : ('Marcia Smith', 'James Johsnon')
drug_providers = {}
#total_vost stores drug name key to total integer value of costs.  Example - 'AMBIEN' : 1500
drug_total_cost = {}


#Return a list split from string input seperated by comma
def listify_line(line):
    return line.split(",")

with open(file_to_open) as f:
    #Skip file headers
    next(f)
    for line in f:
        line = line.strip()
        line = listify_line(line)
        #Concatenate first and last name of provider. Example - 'Marcia Smith'
        provider = line[1] + " " + line[2]
        drug = line[3]
        cost = int(line[4])
        if drug not in drug_providers:
            drug_providers[drug] = set([provider])
            drug_total_cost[drug] = cost
        else:
            #Since drug_provider values are sets, can use add method and repeat names will not be added
            drug_providers[drug].add(provider)
            drug_total_cost[drug] += cost

#Used to create a list of sets of drug and cost.  Example - [(1500, 'AMBIEN), (3000, 'BENZTROPINE MESYLATE')]
all_drugs_cost = []
for drug, total_cost in drug_total_cost.items():
    all_drugs_cost.append((total_cost, drug))

#Sort drug price ascending, if tie, sort drug name ascending
all_drugs_cost.sort(key=lambda x: x[0], reverse=True)

#Create filepath for output text file
output_data_folder = join(dirname(dirname(abspath(__file__))), "output")

#Output to top_drug_cost.txt. Example (one line of file) - CHLROPROMAZINE,2,3000
with open(join(output_data_folder, 'top_drug_cost.txt'), 'w') as drug_cost:
    drug_cost.write('drug_name,num_prescriber,total_cost\n')
    for item in all_drugs_cost:
        drug = item[1]
        cost_of_drug = item[0]
        providers_total = len(drug_providers[drug])
        drug_cost.write(drug + "," + str(providers_total) + "," + str(cost_of_drug) + "\n")
