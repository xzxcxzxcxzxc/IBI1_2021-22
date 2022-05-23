#!python3

import copy
import tkinter as tk
from tkinter import messagebox

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

def codon_list():              #find the initiation codon, each of the codon is placed in a list.
    global codon               #initialize 
    global origin
    codon =[]
    origin = []
    origin = entry1.get().upper()                       #change the input to the capital
    for i in range(len(origin)):
        tkLabel2.set('there are no ATG')
        if origin[i:i+3] == 'ATG':     #find the strat codon, and add the following codon to a list.
            for j in range(i,len(origin),3):                    
                codon.append(origin[j:j+3])                     
                try:
                    if codon_table[origin[j:j+3]] == 'stop':  #if the codon is stop, then stop this function
                        break
                except KeyError:
        #   if the input is not a multiple of three, or input is not ATCG，then exit and ask for re-enter
                    tkLabel2.set('input is not a complete sequence')
                    return False
            tkLabel2.set(codon)                         #print the codon in the visual interface
            break
    origin=codon.copy()
    return True
 
def mutationConsequences():
    global codon          #initialize
    global origin
    mutationPlace = int(entry2.get()) - 1   #assign entry2 to the mutationPlace
    mutationCodon = entry3.get().upper()    #assign entry3 to the mutationCodon
    a = mutationPlace // 3                  #find the mutated codon
    if a == 0 :                             #if the mutation occored in the start codon, then print initiation codon mutated.
        tkLabel6.set('initiation codon mutated')
    else:
        b = mutationPlace % 3               #find the mutated base
        mutation = list(origin[a])
        mutation[b] = mutationCodon         #mutation occur
        c = origin[a]+' changed to: '+''.join(mutation)+'\n'+codon_table[origin[a]]+' changed to: '+codon_table[''.join(mutation)]
        tkLabel6.set(c)      #print origin amino acid and the mutated amino acid in the visual interface 


def synonymosCalculator():
    global codon          #initialize
    synonymous = 0 
    nonsynonymous = 0
    for i in range(len(codon)):    #traverse all the DNA sequence
        for j in range(3):
            mutation = list(codon[i])        #divide the codon into three bases and store each in a list
            for h in basic:
                if not codon[i][j] == h:     #if the mutation do not occor(e.g. A->A), then just go to next loop.
                    mutation[j] = h 
                    if codon_table[''.join(mutation)] == codon_table[codon[i]]:  #if the amino acid changed, then synonymous + 1
                        synonymous += 1
                    else:                                                #if the amino acid do not changed, then nonsynonymous + 1
                        nonsynonymous += 1
    a = 'synonymous number is :' + str(synonymous) + '\nnunsynonymous number is: ' + str(nonsynonymous)
    tkLabel7.set(a)                                                             #print the answer on the visual interface

def vulnerabilityCalculator():
    global codon          #initialize
    vulnerability = 0
    for i in range(len(codon)):    #traverse all the DNA sequence
        for j in range(3):
            mutation = list(codon[i])        #divide the codon into three bases and store each in a list
            for h in basic:
                if not codon[i][j] == h:     #if the mutation do not occor(e.g. A->A), then just go to next loop.
                    mutation[j] = h 
                    if codon_table[''.join(mutation)] == 'stop' and codon_table[codon[i]] != 'stop':   
                        #if a truncating mutation occor, vulnerability + 1
                        vulnerability += 1    
    a = 'vulnerability number is :' + str(vulnerability)
    tkLabel8.set(a)                                      #print the answer on the visual interface

def transitionsCalculator():
    global codon
    transversionsSynonymous = 0
    transversionsNonsynonymous = 0          #initialize
    for i in range(len(codon)):    #traverse all the DNA sequence
        for j in range(3):
            mutation = list(codon[i])        #divide the codon into three bases and store each in a list
            for h in basic:
                if not codon[i][j] == h:     #if the mutation do not occor(e.g. A->A), then just go to next loop.
                    mutation[j] = h 
                    if (h in 'AG' and codon[i][j] in 'CT') or (h in 'CT' and codon[i][j] in 'AG'):    #Determine whether it is transversions mutation
                        if codon_table[''.join(mutation)] == codon_table[codon[i]]:            #if the amino acid changed, the transversionsSynonymous + 1
                            transversionsSynonymous += 1
                        else:                                                        #if the amino acid do not changed, the transversionsNonsynonymous + 1
                            transversionsNonsynonymous += 1
    a = 'transversionsSynonymous number is :' + str(transversionsSynonymous) + '\ntransversionsNonsynonymous number is: ' + str(transversionsNonsynonymous)
    tkLabel9.set(a)                                                                 #print the answer on the visual interface                        

def additionalFunction():       
    global codon                         #initialize 
    codonContent = {'A':0,'T':0,'C':0,'G':0}
    c = 0
    for a in codon:
        for b in a:
            codonContent[b] += 1        #count the number of each bases
            c += 1                      #count the total number of bases
    hydrogenBond = (codonContent['A'] + codonContent['T']) * 2 + (codonContent['G'] + codonContent['C']) * 3        #calculate the number of hydrogen bond
    rate = (codonContent['A'] + codonContent['T']) / c                                                              #Calculate the proportion of 'at'
    a = 'hydrogenBond number is: ' +str(hydrogenBond) + '\nthe rate of AT is: ' + str(rate)
    tkLabel10.set(a)                                                                #print the answer on the visual interface

def allCaculation():
    synonymosCalculator()
    vulnerabilityCalculator()
    transitionsCalculator()
    additionalFunction()


codon = []
origin = []
win = tk.Tk()
win.title('group ica')
win.geometry('630x350')


tkEntry1 = tk.StringVar()
tkEntry2 = tk.StringVar()
tkEntry3 = tk.StringVar()
tkLabel2 = tk.StringVar()
tkLabel6 = tk.StringVar()
tkLabel7 = tk.StringVar()
tkLabel8 = tk.StringVar()
tkLabel9 = tk.StringVar()
tkLabel10 = tk.StringVar()

entry1 = tk.Entry(win,textvariable=tkEntry1,bg='lightblue',validate='focusout',validatecommand=codon_list,width=60)
entry2 = tk.Entry(win,textvariable=tkEntry2,width=10)
entry3 = tk.Entry(win,textvariable=tkEntry3,width=10)
label1 = tk.Label(win,text='please input the DNA sequence:')
label2 = tk.Label(win,textvariable=tkLabel2,wraplength=500)
label3 = tk.Label(win,text='codon is:')
label4 = tk.Label(win,text='input the mutated place:')
label5 = tk.Label(win,text='input the mutated codon:')
label6 = tk.Label(win,textvariable=tkLabel6,wraplength=500)
label7 = tk.Label(win,textvariable=tkLabel7,wraplength=500)
label8 = tk.Label(win,textvariable=tkLabel8,wraplength=500)
label9 = tk.Label(win,textvariable=tkLabel9,wraplength=500)
label10 = tk.Label(win,textvariable=tkLabel10,wraplength=500)
butten1 = tk.Button(win,text='mutation',command=mutationConsequences)
butten2 = tk.Button(win,text='caculation',command=allCaculation)

label1.grid(column=0,row=0)
entry1.grid(column=1,row=0,ipady=10,columnspan=4)
label3.grid(column=0,row=1)
label2.grid(column=1,row=1,columnspan=4)
label4.grid(column=0,row=2)
entry2.grid(column=1,row=2)
label5.grid(column=2,row=2)
entry3.grid(column=3,row=2)
butten1.grid(column=4,row=2)
label6.grid(column=0,row=3,columnspan=5,sticky=tk.W+tk.E+tk.N+tk.S)
label7.grid(column=0,row=4,columnspan=5,sticky=tk.W+tk.E+tk.N+tk.S)
label8.grid(column=0,row=5,columnspan=5,sticky=tk.W+tk.E+tk.N+tk.S)
label9.grid(column=0,row=6,columnspan=5,sticky=tk.W+tk.E+tk.N+tk.S)
label10.grid(column=0,row=7,columnspan=5,sticky=tk.W+tk.E+tk.N+tk.S)
butten2.grid(column=2,row=8,sticky=tk.W)

win.mainloop()
