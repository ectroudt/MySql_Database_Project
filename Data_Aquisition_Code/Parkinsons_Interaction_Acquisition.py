#!/usr/bin/python3.5

import json
import sys
from urllib import request, error


def STRING_id_list(conversion_dict):

    id_list = []

    for prot in conversion_dict:

        id_list.append(prot.get("stringId"))

    return id_list


def STRING_Interaction_Data(gene_id_list):

    string_call = "https://string-db.org/api/"
    string_method = "interaction_partners?"
    out_format = "tsv"
    species = "9606"
    score = "700"
    caller = "ectroudt"

    string_call += out_format + "/" + string_method
    string_call += "identifiers=" + "%0d".join(gene_id_list)
    string_call += "&species=" + species
    string_call += "&required_score=" + score
    string_call += "&caller_identity=" + caller

    try:

        string_req = request.urlopen(string_call)

        with open("Parkinson_STRING_GInt_data_MOD.tsv", "w") as x:

            x.write(string_req.read().decode())

    except error.URLError as err:

        print("\n Problem retrieving STRING data: " + str(err.args[0]) + "\n")
        sys.exit()

    except OSError as addtl_err:

        print("\n Problem retrieving STRING data: " + str(addtl_err.args[1]) + "\n")
        sys.exit()

    except TypeError as bad_file:

        print("\n File is not correct type >> " + str(bad_file.args[0]) + "\n")
        sys.exit()

    except IOError as bad_data:

        print("\n There is file input/output error >> " + str(bad_data.args[1]) + "\n")
        sys.exit()

    except Exception:

        print("\n Something went wrong with either the URL request or the file opening/processing...\n")


def main():

    with open("Parkinson_STRING_Genes.json") as x:

        STRING_data = json.load(x)

    Park_gene_list = STRING_id_list(STRING_data)

    STRING_Interaction_Data(Park_gene_list)


main()

