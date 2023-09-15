# df = pd.read_csv('/media/a40540/results/Holen_sep_Vera/in/usearch_result/hits_amr.b6',sep = '\t',header = None)
# for i in range(len(df)):
#     print(df.iloc[])
for file in ['hits_amr.b6','hits_metal.b6','hits_mge.b6','hits_vfdb.b6']:
    total_data = []
    with open(file,'r') as f1:
        rd_f1 = f1.readlines()
    for each in rd_f1:
        second_column = each.split('\t')[1].strip()
        total_data.append(second_column)
    set_data = set(total_data)
    with open(file.split('.')[0]+'_count.txt','a') as f2:
        f2.write('Gene Name'+'\t'+'Count\n')
    for every in set_data:
        with open(file.split('.')[0]+'_count.txt','a') as f2:
            f2.write(every+'\t'+str(total_data.count(every))+'\n')
#     print(every,total_data.count(every))
