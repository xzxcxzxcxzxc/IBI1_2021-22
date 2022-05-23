#!python3
basic = 'ATCG'

codon_table = {                                             #DNA codon
    'TTT':'Phe','TTC':'Phe','TTA':'Leu','TTG':'Leu',
    'TCT':'Ser','TCC':'Ser','TCA':'Ser','TCG':'Ser',
    'TAT':'Tyr','TAC':'Tyr','TAA':'stop','TAG':'stop',
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

def mutationConsequences(origin):
    initiationSite = True
    mutationPlace = int(input('please input the mutation place'))
    mutationCodon = input('please input mutated base').upper()
    a = mutationPlace // 3
    if a == 0 :
        initiationSite = False
    b = mutationPlace % 3 - 1
    mutation = list(origin[a])
    mutation[b] = mutationCodon
    return codon_table[''.join(mutation)],codon_table[origin[a]],origin[a][b],mutationCodon,initiationSite


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

def additionalFunction(origin):       #额外还没想法，下次一定.
    codonContent = {'A':0,'T':0,'C':0,'G':0}
    c = 0
    for a in codon:
        for b in a:
            codonContent[b] += 1
            c += 1
    hydrogenBond = (codonContent['A'] + codonContent['T']) * 2 + (codonContent['G'] + codonContent['C']) * 3
    rate = (codonContent['A'] + codonContent['T']) / c
    return hydrogenBond,rate

while True:
    codon = []
    dnaOrigin = input('Please enter the DNA sequence: ').upper()
    judge = codon_list(dnaOrigin)
    if judge and codon != []:
        mutatedAmino,originAmino,originCodon,mutatedCodon,initiationSite = mutationConsequences(codon)
        if initiationSite:
            print(' origin amino acid is:',originAmino,'\n mutated amino acid is:', mutatedAmino,'\n the codon change from: ',originCodon,' to: ',mutatedCodon)
        else:
            print('Initial site is mutated')
        synonymous,nonsynonymous = synonymosCalculator(codon)
        print(' synonymous:',synonymous,'\n nonsynonymous:',nonsynonymous)
        vulnerability = vulnerabilityCalculator(codon)
        print(' vulnerability:',vulnerability)
        transversionsSynonymous,transversionsNonsynonymous = transitionsCalculator(codon)
        print(' transversionsSynonymous:',transversionsSynonymous,'\n transversionsNonsynonymous:',transversionsNonsynonymous)
        print(' the rate of transversions nonsynonymous is: ',transversionsNonsynonymous/transversionsSynonymous)
        print(' the rate of transitions nonsynonymous is: ',(nonsynonymous-transversionsNonsynonymous)/(synonymous-transversionsSynonymous))
        hydrogenBond,rate = additionalFunction(codon)
        print(' hydrogen bond:',hydrogenBond,'\n the rate of A and T is: ',rate)
    else:
        print('input is not a complete sequence')