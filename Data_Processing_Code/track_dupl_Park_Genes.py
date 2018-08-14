import sys
import json

sys.path.append('./Data_Aquisition_Code')

from Parkinsons_DataAquisition import MIM_gene_aquisition

park_genes = MIM_gene_aquisition()
with open("Parkinson_STRING_Genes.json") as x:

    STRING_data = json.load(x)

STRING_gene_list = []


for label in STRING_data:

    STRING_gene_list.append(str(label.get("preferredName")))

for MIM_gene in park_genes:

    if MIM_gene not in STRING_gene_list:

        print(MIM_gene)

print(len(STRING_gene_list))