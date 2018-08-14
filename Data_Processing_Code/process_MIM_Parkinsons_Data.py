
with open("/home/eric/CSCI_8876/Database_Project/Phenotypic-Series-PS168600.txt") as x:

    MIM_gene_data = x.readlines()


with open("/home/eric/CSCI_8876/Database_Project/Parkinsons_Phenotypes_processed.tsv", "w") as outfile:

    for record in MIM_gene_data:
        record.rstrip("\n")
        MIM_gene_record = record.split("\t")

        if len(MIM_gene_record) != 7:
            pass

        elif "Gene/Locus" in record:
            pass

        else:
            outfile.write(str(MIM_gene_record[4]) + "\t" + str(MIM_gene_record[1])
                          + "\t" + str(MIM_gene_record[2]) + "\t" + str(MIM_gene_record[5])
                          + "\t" + str(MIM_gene_record[6].rstrip("\n")) + "\n")

