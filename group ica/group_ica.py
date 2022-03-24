#!python3

basic = 'ATCG'

codon_table = {                                             #DNA codon
    'TTT':'Phe','TTC':'Phe','TTA':'Leu','TTG':'Leu',
    'TCT':'SER','TCC':'SER','TCA':'SER','TCG':'SER',
    'TAT':'Tyr','TAC':'TyR','TAA':'stop','TAG':'stop',
    'TGT':'Cys','TGC':'Cys','TGA':'stop','TGG':'Trp',
    'CTT':'Leu','CTC':'Leu','CTA':'Leu','CTG':'Leu',
    'CCT':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
    'CAT':'His','CAC':'His','CAA':'Gin','CAG':'Gin',
    'CGT':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg',
    'ATT':'Ile','ATC':'Ile','ATA':'Ile','ATG':'Met',
    'ACT':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr',
    'AAT':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys',
    'AGT':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg',
    'GTT':'Val','GTC':'Val','GTA':'Val','GTG':'Val',
    'GCT':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala',
    'GAT':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu',
    'GGT':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly',
}

codon = []

def codon_list(origin):
    global codon
    for i in range(len(origin)):
        if origin[i:i+3] == 'ATG':  #加一个是否为三的判断
            for j in range(i,len(origin),3):
                codon.append(origin[j:j+3])
                if codon_table[origin[j:j+3]] == 'stop':
                    break
            print(codon)
            break                   #TODO假如序列中存在ATG，可删除并修改。

def mutationConsequences():
    pass                            #没看懂题目，不好意思

def synonymosCalcilator(origin):
    synonymous = 0
    nonsynonymous = 0
    vulnerability = 0
    transversionsSynonymous = 0
    transversionsNonsynonymous = 0
    for i in range(len(origin)):
        for j in range(3):
            mutation = []
            for a in range(3):              #TODO字符串可直接转为列表
                mutation.append(origin[i][a]) 
            for h in basic:
                if origin[i][j] == h:
                    continue
                else:
                    mutation[j] = h
                    print(''.join(mutation))
                    if codon_table[''.join(mutation)] == codon_table[origin[i]]:
                        synonymous += 1
                        if (h in 'AG' and origin[i][j] in 'CT') or (h in 'CT' and origin[i][j] in 'AG'):
                            transversionsSynonymous += 1
                    else:
                        nonsynonymous += 1
                        if (h in 'AG' and origin[i][j] in 'CT') or (h in 'CT' and origin[i][j] in 'AG'):
                            transversionsNonsynonymous += 1
                    if codon_table[''.join(mutation)] == 'stop' and codon_table[origin[i]] != 'stop':
                        vulnerability += 1    
    return synonymous,nonsynonymous,vulnerability,transversionsSynonymous,transversionsNonsynonymous


def additionalFunction():       #额外还没想法，下次一定.
    pass


dnaOrigin = input()
codon_list(dnaOrigin)
a,b,c,d,f = synonymosCalcilator(codon)
print(' synonymous:',a,'\n nonsynonymous:',b,'\n vulnerability',c,'\n transversionsSynonymous:',d,'\n transversionsNonsynonymous:',f)