import os
pwd = os.getcwd()
list_of_files = os.listdir(pwd)
print(list_of_files)
for each in list_of_files:
    if(('_R1_' in each) and ('_val_1.fq' in each)):
        forward_read = each
        break
os.system(("{software} \
        -usearch_global {sequence1} \
        -db {DBpath} \
        -evalue 0.00001 \
        -id 0.9 \
        -query_cov 1 \
        -blast6out {DB_destination} \
        -strand {direction} \
        -maxaccepts 1 \
        -threads 128").\
        format(direction = 'plus', \
               software = 'usearch', \
               sequence1 = forward_read, \
               DBpath = '/localscratch/vfdb.udb', \
               DB_destination = 'hits_vfdb.b6')) 
