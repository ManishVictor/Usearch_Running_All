import pandas as pd
total_data = []
file = 'names_sorted_amr_counts.txt'
with open(file,'r') as f1:
    rd_f1 = f1.readlines()
for each in rd_f1:
    second_column = each.split('\t')[0].strip()
    total_data.append(second_column)
set_data = set(total_data)
with open(file.split('.')[0]+'_final.txt','a') as f2:
    f2.write('Gene Name'+'\t'+'Count\n')
for every in set_data:
    tot_count = 0
    for line in rd_f1:
       name,count = line.rstrip('\n').split('\t')
       if(every == name):
           tot_count += pd.to_numeric(count)
    with open(file.split('.')[0]+'_final.txt','a') as f2:
        f2.write(every+'\t'+str(tot_count)+'\n')
