import re

seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'

a = re.findall('GAATTC', seq)

print('there will be',len(a) + 1,'seqs after cutting')