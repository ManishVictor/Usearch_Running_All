with open('hits_amr_count.txt') as file1:
    re_file1 = file1.readlines()
for i in range(1,len(re_file1)):
    line = re_file1[i].rsplit('\n')
    name,count = line[0].split('\t')
    ncbi_name = name.split('~~~')[1]
    if(ncbi_name.startswith('(')):
        for j in range(len(ncbi_name)):
            if(')' == ncbi_name[j]):
                print(j+1)
                break
            else:
                continue
        with open('names_sorted_amr_counts.txt','a') as file3:
            file3.write(('{}\t{}\n').format(ncbi_name[j+1:],count))
    else:
        with open('names_sorted_amr_counts.txt','a') as file4:
            file4.write(('{}\t{}\n').format(ncbi_name,count))
