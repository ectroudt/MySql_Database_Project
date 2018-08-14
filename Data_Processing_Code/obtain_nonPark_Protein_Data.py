#!/usr/bin/python3.5

from Int_Data_Parse import get_ParkGene_Names, get_Int_Data


def get_nonPark_Proteins():

    non_park_proteins = {}

    park_genes = get_ParkGene_Names()
    park_interactions = get_Int_Data()

    for int_record in park_interactions:

        if str(int_record[1]) == "stringId_B":

            pass

        else:

            STRING_ID = str(int_record[1])
            prot_common_name = str(int_record[3])

            if not(non_park_proteins.get(STRING_ID, False)) and (prot_common_name not in park_genes):

                non_park_proteins[STRING_ID] = prot_common_name

    return non_park_proteins


def main():

    nonPark_proteins = get_nonPark_Proteins()

    with open("non_parkinsons_proteins.tsv", "w") as outfile:

        outfile.write("stringId" + "\t" + "preferredName" + "\n")

        for id, name in nonPark_proteins.items():

            outfile.write(str(id + "\t" + str(name) + "\n"))


if __name__ == '__main__':

    main()




