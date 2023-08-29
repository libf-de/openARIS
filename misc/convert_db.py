#!/usr/bin/env python3

"""Export to CSV."""
import sys
import csv
from dbfread import DBF

if sys.argv[1] is None:
    print(f"Usage: {sys.argv[0]} <dbf-file>")
    exit(1)

table = DBF(sys.argv[1], encoding='cp850')
writer = csv.writer(sys.stdout)

writer.writerow(table.field_names)
for record in table:
    writer.writerow(list(record.values()))