import re

seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'

a = re.findall('GAATTC', seq)

print(len(a) + 1)