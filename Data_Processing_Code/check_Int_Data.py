#!/usr/bin/python3.5

from Int_Data_Parse import get_ParkGene_Names, get_Int_Data


def main():

    park_genes = get_ParkGene_Names()
    park_interactions = get_Int_Data()

    dupl_interactions = []

    for record in park_interactions:

        if str(record[3]) in park_genes:

            dupl_interactions.append(str(record))

    if dupl_interactions:

        for int_rec in dupl_interactions:

            print(int_rec)

    print(len(dupl_interactions))


if __name__ == '__main__':

    main()