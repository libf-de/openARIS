#!/usr/bin/env python

# Skript, welches DBF-Datenbanken für FN ARIS
# entschlüsselt und als CSV ausgibt.
# Das Verschlüsselungsverfahren funktioniert so,
# dass die Zeichen je nach ihrer Position um
# n Stellen in der ASCII-Tabelle vor/zurück geschoben
# werden. Die MAGIC_NUMBER gibt an, um wie viele
# Stellen an der jeweiligen Position verschoben wird.
# Zum Entschlüsseln wird addiert, zum Verschlüsseln
# subtrahiert.

import sys
import csv
from dbfread import DBF

if sys.argv[1] is None:
    print(f"Usage: {sys.argv[0]} <dbf-file>")
    exit(1)

FIELDS_TO_DECRYPT = ['STRASSE', 'PLZ', 'ORT', 'TEL1', 'FAX', 'EMAIL']
INDICES_TO_DECRYPT= []
MAGIC_NUMBER = "9116495929116594939116495949116594959911659496911649597911659498"

def decrypt(inp_str: str):
    ascii_nums = [ord(x) for x in inp_str]
    for i in range(0, len(inp_str)):
        if ascii_nums[i] > 127:
            continue
        ascii_nums[i] += int(MAGIC_NUMBER[i])
    return ''.join(chr(i) for i in ascii_nums)

def encrypt(inp_str: str):
    ascii_nums = [ord(x) for x in inp_str]
    for i in range(0, len(inp_str)):
        if ascii_nums[i] > 127:
            continue
        ascii_nums[i] -= int(MAGIC_NUMBER[i])
    return ''.join(chr(i) for i in ascii_nums)

table = DBF(sys.argv[1], encoding='cp850')
writer = csv.writer(sys.stdout)

writer.writerow(table.field_names)

for field in FIELDS_TO_DECRYPT:
    if field in table.field_names:
        INDICES_TO_DECRYPT.append(table.field_names.index(field))

for record in table:
    vals = list(record.values())
    for i in INDICES_TO_DECRYPT:
        vals[i] = decrypt(vals[i])
    writer.writerow(vals)