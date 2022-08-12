import json
import csv

def json_to_tsv(jname, tsv):
    f = open(jname)
    items = json.load(f)
    output = open(tsv, 'w')
    dw = csv.DictWriter(output, sorted(items[0].keys()), delimiter='\t')
    dw.writeheader()
    dw.writerows(items)

json_to_tsv("jason.json", "tsv3.tsv")