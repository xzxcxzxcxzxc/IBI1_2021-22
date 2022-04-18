
def calculator(seq):
    for i in seq:
        nucleotides[i] += 1
nucleotides = {'A':0,'T':0,'C':0,'G':0}
seq = input('input your DNA sequence').upper()
calculator(seq)
print(nucleotides.items())