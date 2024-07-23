import os

folder_path = 'C:\\Users\\alcen\\OneDrive\\Рабочий стол\\hw.files_txt\\file_with_txt'
def parse_folder(path):

    for root, dirs, files in os.walk(folder_path, topdown=False): 
        files_names = []     
        for name in files:
            files_names.append(name)
        print(files_names)
        return files_names
    
def read_from_folder(path):
    for file in os.listdir(folder_path):
        with open(file) as f:
            files = []
            files.append(file.readlines())
            print(files)
            return files


def len_of_files(path):
    for file in os.listdir(folder_path):
        with open(file) as f:        
            len_f = []            
            f.readlines()
            len_f.append(len(f))
        s_len_f = sorted(len_f)
        print(s_len_f)
            
    
parse_folder(folder_path)    
read_from_folder(folder_path)
len_of_files(folder_path)






    
'''   
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

        
'''       
    

  

  
