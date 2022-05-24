import os
seq1 = "MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY"
seq2 = "MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAGYPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY"
randSeq = 'GDYHNIYEMQSTDNDVIIVLCESYWQNRYWCGYKQNCIFEDSSLFAPSEVDWAVNGYPPYRAVNMHKYEYDYATPTPQKMMWWHLPIWSWHFWGWNIRTWDILTNSGNTMGFCYCAWVCNLPCMILCHARFAFSTDKKPFSVHTFIIKICHTQPALAVTEPNADSCCMIFPLIGKSYCHTCGTWDFYPNEVKYQFNFSAATQYENVIYIFHHICQDVRRGCTDIELNHFWMSHHVANRKLENIVGYRAILRFIGSKCAQNMRSLFAHPWQSFQDHKEYDWHGNLGLNWP'

aminoacid = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X']
matirx=[[4,-1,-2,-2,0,-1,-1,0,-2,-1,-1,-1,-1,-2,-1,1,0,-3,-2,0,-2,-1],
        [-1,5,0,-2,-3,1,0,-2,0,-3,-2,2,-1,-3,-2,-1,-1,-3,-2,-3,-1,0],
        [-2,0,6,1,-3,0,0,0,1,-3,-3,0,-2,-3,-2,1,0,-4,-2,-3,3,0],
        [-2,-2,1,6,-3,0,2,-1,-1,-3,-4,-1,-3,-3,-1,0,-1,-4,-3,-3,4,1],
        [0,-3,-3,-3,9,-3,-4,-3,-3,-1,-1,-3,-1,-2,-3,-1,-1,-2,-2,-1,-3,-3],
        [-1,1,0,0,-3,5,2,-2,0,-3,-2,1,0,-3,-1,0,-1,-2,-1,-2,0,3],
        [-1,0,0,2,-4,2,5,-2,0,-3,-3,1,-2,-3,-1,0,-1,-3,-2,-2,1,4],
        [0,-2,0,-1,-3,-2,-2,6,-2,-4,-4,-2,-3,-3,-2,0,-2,-2,-3,-3,-1,-2],
        [-2,0,1,-1,-3,0,0,-2,8,-3,-3,-1,-2,-1,-2,-1,-2,-2,2,-3,0,0],
        [-1,-3,-3,-3,-1,-3,-3,-4,-3,4,2,-3,1,0,-3,-2,-1,-3,-1,3,-3,-3],
        [-1,-2,-3,-4,-1,-2,-3,-4,-3,2,4,-2,2,0,-3,-2,-1,-2,-1,1,-4,-3],
        [-1,2,0,-1,-3,1,1,-2,-1,-3,-2,5,-1,-3,-1,0,-1,-3,-2,-2,0,1],
        [-1,-1,-2,-3,-1,0,-2,-3,-2,1,2,-1,5,0,-2,-1,-1,-1,-1,1,-3,-1],
        [-2,-3,-3,-3,-2,-3,-3,-3,-1,0,0,-3,0,6,-4,-2,-2,1,3,-1,-3,-3],
        [-1,-2,-2,-1,-3,-1,-1,-2,-2,-3,-3,-1,-2,-4,7,-1,-1,-4,-3,-2,-2,-1],
        [1,-1,1,0,-1,0,0,0,-1,-2,-2,0,-1,-2,-1,4,1,-3,-2,-2,0,0],
        [0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,1,5,-2,-2,0,-1,-1],
        [-3,-3,-4,-4,-2,-2,-3,-2,-2,-3,-2,-3,-1,1,-4,-3,-2,11,2,-3,-4,-3],
        [-2,-2,-2,-3,-2,-1,-2,-3,2,-1,-1,-2,-1,3,-3,-2,-2,2,7,-1,-3,-2],
        [0,-3,-3,-3,-1,-2,-2,-3,-3,3,1,-2,1,-1,-2,-2,0,-3,-1,4,-3,-2],
        [-2,-1,3,7,-3,0,1,-1,0,-3,-4,0,-3,-3,-2,0,-1,-4,-3,-3,4,1],
        [-1,0,0,1,-3,3,4,-2,0,-3,-3,1,-1,-3,-1,0,-1,-3,-2,-2,1,4],
        [0,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,0,0,-2,-1,-1,-1,-1]]
editDistance = 0 
for i in range(len(seq1)):
    a = aminoacid.index(seq1[i])
    b = aminoacid.index(seq2[i])
    editDistance += matirx[a][b]
print('the distance between human and mouse is',editDistance)
editDistance = 0 
for i in range(len(seq1)):
    a = aminoacid.index(randSeq[i])
    b = aminoacid.index(seq2[i])
    editDistance += matirx[a][b]
print('the distance between human and random sequence is',editDistance)
editDistance = 0 
for i in range(len(seq1)):
    a = aminoacid.index(seq1[i])
    b = aminoacid.index(randSeq[i])
    editDistance += matirx[a][b]
print('the distance between mouse and random sequence is',editDistance)