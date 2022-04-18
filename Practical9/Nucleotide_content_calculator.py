
def calculator(seq):
    b = 0
    for i in seq:
        nucleotides[i] += 1
        b += 1
    for i in 'ATCG':
        nucleotides[i] /= b
nucleotides = {'A':0,'T':0,'C':0,'G':0}
#seq = input('input your DNA sequence').upper()
seq = 'atgctactagctgcATCGCTAGCTAGCTAGCTAGCTAGCTAGTACGCagctacgtagctagctagctagctagctgcgtgtacgtacgtacgtcagtacgtgatttagactgactgtacg'.upper()
calculator(seq)
print(nucleotides.items())