
with open("non_Park_Proteins_Revised.tsv") as prot_file:
    prot_file = prot_file.readlines()

    for prot_rec in prot_file:
        prot_rec = prot_rec.split("\t")

        prot_name = str(prot_rec[1])
        prot_terms = str(prot_rec[2])

        if "ENSG" in str(prot_name) or prot_terms == " ":
            print(str(prot_name) + " " + str(prot_terms))