#with open('text_1.txt', 'a', encoding = 'utf-8') as file_1, open ('text_2.txt', 'a', encoding = 'utf-8') as file_2, open ('text_3.txt', 'a', encoding = 'utf-8') as file_3:
    

with open('text_1.txt', encoding = 'utf-8') as file_1, open ('text_2.txt', encoding = 'utf-8') as file_2, open ('text_3.txt', encoding = 'utf-8') as file_3:
    
        
    files = (file_1.readlines()), file_2.readlines(), file_3.readlines()
    len_f = []
    for f in files:
        len_f.append(len(f))
    s_len_f = sorted(len_f)

with open('text_1.txt', encoding = 'utf-8') as file_1, open ('text_2.txt', encoding = 'utf-8') as file_2, open ('text_3.txt', encoding = 'utf-8') as file_3:
        
    files_for_dict = (file_1.read().rstrip(), file_2.read().rstrip(), file_3.read().rstrip())
    dict_f = dict(zip(len_f, files_for_dict))
    sort_dict_f = dict(sorted(dict_f.items())) 
    

       
      

   

with open('comb_file.txt', 'a', encoding = 'utf-8') as c_f:

    c_f.write('text_1.txt' + '\n')
    c_f.write(str(list(sort_dict_f.keys())[0]) + '\n')
    c_f.writelines(str(list(sort_dict_f.values())[0]) + '\n')
    c_f.write('text_2.txt' + '\n')
    c_f.write(str(list(sort_dict_f.keys())[1]) + '\n')
    c_f.writelines(str(list(sort_dict_f.values())[1]) + '\n')
    c_f.write('text_3.txt' + '\n')
    c_f.write(str(list(sort_dict_f.keys())[2]) + '\n')
    c_f.writelines(str(list(sort_dict_f.values())[2]))

        
       
    

  

  
   
          