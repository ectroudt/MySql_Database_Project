#!/usr/bin/python3.5

import json

def get_gene_MIM_dict():

    with open("Phenotypic-Series-PS168600.txt") as x:

        MIM_gene_data = x.readlines()

        gene_MIMnum_dict = {}

        for record in MIM_gene_data:
            record.rstrip("\n")
            MIM_gene_record = record.split("\t")

            if len(MIM_gene_record) != 7:
                pass

            elif "Gene/Locus" in record:
                pass

            else:

                gene_MIMnum_dict[str(MIM_gene_record[5].split(",")[0])] = MIM_gene_record[6]

    return gene_MIMnum_dict



def main():

    with open("Parkinson_STRING_Genes.json") as x:

        STRING_data = json.load(x)

    with open("Parkinson_STRING_Genes_processed.tsv", "w") as outfile:

        gene_MIMs = get_gene_MIM_dict()

        for label in STRING_data:

            stringID = label.get("stringId")[5:]
            geneName = label.get("preferredName")

            mimnum = None

            for genes in gene_MIMs.keys():

                if geneName in str(genes):

                    mimnum = gene_MIMs.get(genes).rstrip("\n")

            ncbiTaxon = label.get("ncbiTaxonId")
            gene_annot = label.get("annotation")

            outfile.write(str(stringID) + "\t" + str(geneName) + "\t" + str(ncbiTaxon) + "\t" + str(gene_annot) +
                          "\t" + str(mimnum) + "\n")


main()