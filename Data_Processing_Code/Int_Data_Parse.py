#!/usr/bin/python3.5

import json


def get_Int_Data():

    int_Data = []

    with open("Parkinson_STRING_GInt_data.tsv") as int_file:

        interaction_data = int_file.readlines()

        for record in interaction_data:

            int_Data.append(record.split("\t"))

    return int_Data


def get_ParkGene_Names():

    pref_Gene_Names = []

    with open("Parkinson_STRING_Genes.json") as x:

        STRING_data = json.load(x)

    for label in STRING_data:

        pref_Gene_Names.append(str(label.get("preferredName")))

    return pref_Gene_Names


def main():

    non_Park_Interactors = []

    gene_names = get_ParkGene_Names()
    gene_interactions = get_Int_Data()

    count = 0

    for i in range(1, len(gene_interactions)):

        if str(gene_interactions[i][2]) not in gene_names:

            non_Park_Interactors.append(str(gene_interactions[i]))

        else:

            count += 1

    if non_Park_Interactors:

        for int_record in non_Park_Interactors:

            print(str(int_record))

    print(count)


if __name__ == '__main__':

    main()