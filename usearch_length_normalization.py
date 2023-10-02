import os
import pandas as pd
######################
def normalization(C_val,L_val,s16):
    formula = ((pd.to_numeric(C_val)/pd.to_numeric(L_val))*151)/s16
    return(formula)
#######################
pwd = os.getcwd()
lof = os.listdir(pwd)
for every in lof:
    if(('count' in every) and ('amr' in every)):
        hits_amr = every
    if(('count' in every) and ('biocide' in every)):
        hits_biocide = every
    if(('count' in every) and ('metal' in every)):
        hits_metal = every
    if(('count' in every) and ('mge' in every)):
        hits_mge = every
    if(('count' in every) and ('vfdb' in every)):
        hits_vfdb = every
dictionary_count_len = {hits_amr:'amr_LEN.txt',\
                        hits_biocide:'biocide_LEN.txt',\
                        hits_metal:'metal_LEN.txt',\
                        hits_mge:'mge_LEN.txt',\
                        hits_vfdb:'vfdb_LEN.txt'}
s16length = 1550
for each in dictionary_count_len:
    count_filename = each
    length_filename = dictionary_count_len[each]
    with open(count_filename,'r') as f1:
        read_f1 = f1.readlines()
    with open(length_filename,'r') as f2:
        read_f2 = f2.readlines()
    for i in range(1,len(read_f1)):
        cname,ccount = read_f1[i].rstrip('\n').split('\t')
        for j in range(len(read_f2)):
            lname,llen = read_f2[j].rstrip('\n').split('\t')
            if(cname == lname):
                value = normalization(ccount,llen,s16length)
                with open(('normalized_{}').format(count_filename),'a') as f3:
                    f3.write(('{}\t{}\n').format(cname,value))
