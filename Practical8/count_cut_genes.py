import re
name = input('Please input the fastq name:')
fileName = open('./' + name)
newFile = open('./new_' + name,'w')
seq = fileName.read()
pattern = re.compile('>.*?gene:(.*?) .*?Acc:.*?]\s([ATCG\n]{10,})',re.S)
seq_list = pattern.findall(seq)
for i in range(len(seq_list)):
    if 'GAATTC' in seq_list[i][1]:
        a = re.sub(r'\n','',seq_list[i][1])
        b = re.findall('GAATTC', a)
        newFile.write('>' + f'{seq_list[i][0]:10}{len(b) + 1:10d}' + '\n')
        newFile.write(a + '\n')
fileName.close()
newFile.close()