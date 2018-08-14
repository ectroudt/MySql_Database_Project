import urllib.parse, urllib.request
from obtain_nonPark_Protein_Data import get_nonPark_Proteins

def remain_Prot():

    non_Park_Prots = get_nonPark_Proteins()
    print(len(non_Park_Prots))

    with open("non_Park_Proteins_Revised.tsv") as prot_file:

        prot_file = prot_file.readlines()

        for prot_rec in prot_file:
            prot_rec = prot_rec.split("\t")

            prot_ID = str(prot_rec[0])

            if non_Park_Prots.get(prot_ID, None) is not None:

                non_Park_Prots.pop(prot_ID)

    return non_Park_Prots


def uniprotID_Aquisition(entryName):

    paramters = {"from": "STRING_ID", "to": "ACC", "format": "tab", "query": entryName}
    param_Encoded = urllib.parse.urlencode(paramters)
    param_Encoded = param_Encoded.encode('utf-8')
    uniProt_url = "http://www.uniprot.org/uploadlists/"

    email_contact = "ectroudt@unomaha.edu"

    uniProt_req = urllib.request.Request(url=uniProt_url, data=param_Encoded, headers={"User-Agent": 'Python %s'
                                                                                                 % email_contact})
    r = urllib.request.urlopen(uniProt_req)

    with open("Uniprot_sample", "w") as x:

        x.write(r.read().decode())


def main():

    non_Park_Prots = remain_Prot()
    print(len(non_Park_Prots))

    rec_count = 0

    for prot, name in non_Park_Prots.items():

        string_prot = "9606." + str(prot)

        uniprotID_Aquisition(str(string_prot))

        with open("Uniprot_sample") as prot_recs:

            prot_recs = prot_recs.readlines()

            if len(prot_recs) > 1:

                rec_count += 1

                line = prot_recs[1]

                line = line.split("\t")

            else:

                line = None
                print(str(prot))

            with open("non_Park_Proteins_Revised.tsv", "a") as sql_recs:

                if line is not None:

                    sql_recs.write(str(prot) + "\t" + str(name) + "\t" + (line[5]) + "\t" + str(line[6]) + "\t"
                                   + str(line[2] + "\n"))

                else:

                    pass

    print(rec_count)


if __name__ == '__main__':

    main()


