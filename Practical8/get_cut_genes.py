import re
fileName = open('./Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
newFile = open('./cut_genes.fa','w')
seq = fileName.read()
#pattern = re.compile('(.*?)[_| ].*?Acc:.*?](.*?)>',re.S)
pattern = re.compile('>.*?gene:(.*?) .*?Acc:.*?]\s([ATCG\n]{10,})',re.S)
seq_list = pattern.findall(seq)
for i in range(len(seq_list)):
    if 'GAATTC' in seq_list[i][1]:
        a = re.sub(r'\n','',seq_list[i][1])
        newFile.write('>' +  f'{seq_list[i][0]:10}{len(a):10d}' + '\n')
        newFile.write(a + '\n')
fileName.close()
newFile.close()