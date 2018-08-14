#!/usr/bin/python3.5

from urllib import request


def MIM_gene_aquisition():

    dupl_count = 0

    parkinsons_MIM_Genes = []

    with open("Phenotypic-Series-PS168600.txt") as x:

        MIM_gene_data = x.readlines()

        for record in MIM_gene_data:
            record.rstrip("\n")
            MIM_gene_record = record.split("\t")

            if len(MIM_gene_record) != 7:
                pass

            elif "Gene/Locus" in record:
                pass

            else:
                gene_name = str(MIM_gene_record[5].split(",")[0])

                if gene_name not in parkinsons_MIM_Genes:

                    parkinsons_MIM_Genes.append(gene_name)

                else:

                    dupl_count += 1


    return parkinsons_MIM_Genes


def STRING_identifier_conv(gene_list):

    string_call = "https://string-db.org/api/"
    string_method = "get_string_ids?"
    out_format = "json"
    species = "9606"
    limit = "1"
    caller = "ectroudt"

    string_call += out_format + "/" + string_method
    string_call += "identifiers=" + "%0d".join(gene_list)
    string_call += "&species=" + species
    string_call += "&limit=" + limit
    string_call += "&caller_identity=" + caller

    string_req = request.urlopen(string_call)

    with open("/home/eric/CSCI_8876/Database_Project/Parkinson_STRING_Genes.json", "w") as x:

            x.write(string_req.read().decode())


def main():

    Parkinsons_Genes = MIM_gene_aquisition()

    STRING_identifier_conv(Parkinsons_Genes)



if __name__ == '__main__':


    main()
