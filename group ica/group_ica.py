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

def codon_list(origin):                                         #find the initiation codon, each of the codon is placed in a list.
    for i in range(len(origin)):
        if origin[i:i+3] == 'ATG': 
            for j in range(i,len(origin),3):                    
                codon.append(origin[j:j+3])                     
                try:
                    if codon_table[origin[j:j+3]] == 'stop':
                        break
                except KeyError:                                #if the input is not a multiple of three，then exit and ask to re-enter
                    return False
            print(codon)
            break
    return True                                                 #TODO假如序列中存在ATG，可删除并修改。

def mutationConsequences():
    pass                                                        #没看懂题目，不好意思

def synonymosCalculator(origin):
    synonymous = 0
    nonsynonymous = 0
    for i in range(len(origin)):
        for j in range(3):
            mutation = list(origin[i])                          #Divide the codon into three bases and store each in a list
            for h in basic:
                if origin[i][j] == h:                           #if the mutation do not occor(e.g. A->A), then just go to next loop.
                    continue
                else:
                    mutation[j] = h                             #mutation occor
                    if codon_table[''.join(mutation)] == codon_table[origin[i]]:                    #if the amino acid changed, then synonymous + 1
                        synonymous += 1
                    else:
                        nonsynonymous += 1
    return synonymous,nonsynonymous

def vulnerabilityCalculator(origin):
    vulnerability = 0
    for i in range(len(origin)):
        for j in range(3):
            mutation = list(origin[i]) 
            for h in basic:
                if origin[i][j] == h:
                    continue
                else:
                    mutation[j] = h
                    if codon_table[''.join(mutation)] == 'stop' and codon_table[origin[i]] != 'stop':   #if a truncating mutation occor, vulnerability + 1
                        vulnerability += 1    
    return vulnerability

def transitionsCalculator(origin):
    transversionsSynonymous = 0
    transversionsNonsynonymous = 0
    for i in range(len(origin)):
        for j in range(3):
            mutation = list(origin[i])
            for h in basic:
                if origin[i][j] == h:
                    continue
                else:
                    mutation[j] = h
                    if (h in 'AG' and origin[i][j] in 'CT') or (h in 'CT' and origin[i][j] in 'AG'):    #Determine whether it is transversions mutation
                        if codon_table[''.join(mutation)] == codon_table[origin[i]]:
                            transversionsSynonymous += 1
                        else:
                            transversionsNonsynonymous += 1
    return transversionsSynonymous,transversionsNonsynonymous

def additionalFunction():       #额外还没想法，下次一定.
    pass

while True:
    codon = []
    dnaOrigin = input('Please enter the DNA sequence: ').upper()
    judge = codon_list(dnaOrigin)
    if judge and codon != []:
        synonymous,nonsynonymous = synonymosCalculator(codon)
        vulnerability = vulnerabilityCalculator(codon)
        transversionsSynonymous,transversionsNonsynonymous = transitionsCalculator(codon)
        print(' synonymous:',synonymous,'\n nonsynonymous:',nonsynonymous,'\n vulnerability',vulnerability)
        print(' transversionsSynonymous:',transversionsSynonymous,'\n transversionsNonsynonymous:',transversionsNonsynonymous)
    else:
        print('input is not a complete sequence')