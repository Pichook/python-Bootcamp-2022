import json
import csv
import os

def json_to_tsv(jname, tsv):
    if os.path.exists(jname):
        f = open(jname)
        items = json.load(f)
        output = open(tsv, 'w')
        dw = csv.DictWriter(output, sorted(items[0].keys()), delimiter='\t')
        dw.writeheader()
        dw.writerows(items)
        return 1
    else:
        return 0

print(json_to_tsv("js.json", "tsv.tsv"))