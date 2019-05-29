# Entry point of the application.

import numpy as np
import string
import sys

ALL_CHARS = string.ascii_lowercase

SUPPORTED_TYPES = {
     'char': {
             'min': '',
             'max': ''
     },
     'int': {
         'min': '',
         'max': ''
     }
    # Other data types can now be easily be
    # appended, along with expected args.
}

try:
    SIZE = sys.argv[1]
    if not isinstance(SIZE, int):
        raise TypeError
except (IndexError, TypeError):
    print('''[WARN] Dataset size not mentioned or invalid.
             Using defaults, 1000 rows.''')
    SIZE = 1000


# [Get header names]
ctr = 1
headers = []
while True:
    header = {}
    header['name'] = input('Header {}: '.format(ctr))
    if header['name'] == '':
        break
    headers.append(header)
    ctr += 1


# [Get header data-type and ranges]
for header in headers:
    header_info_string = str(input('> Type for {}: '.format(header['name']))).lower().split()
    header['type'] = header_info_string[0]
    if header['type'] not in SUPPORTED_TYPES.keys():
        exit('Invalid data type. Aborting.') 
    header['min'] = int(header_info_string[1])
    header['max'] = int(header_info_string[2])


file_name = input('>> File name to save as: ')
if '.csv' not in file_name:
    file_name += '.csv'

with open(file_name, 'w') as f:
    rows = ''
    for header in headers:
        rows += header['name'] + ','
    f.write(rows)

    for i in range(SIZE):
        for header in headers:
            row = ''
            if header['type'] == 'int':
                row += str(np.random.randint(header['min'], header['max']))
            elif header['type'] == 'char':
                random_string = ''
                for x in range(np.random.randint(header['min'], header['max'])):
                    random_string += ALL_CHARS[np.random.randint(0, 25)]
                row += random_string + ','
            f.write(row)
        f.write('\n')
