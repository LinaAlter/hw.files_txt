def counting_lines(files):
    
    dict_line_count = {}
    for file in files:
        with open(file, encoding='utf-8') as txt_f:
            lines_numb = sum(1 for line in txt_f)
        dict_line_count[file] = lines_numb
    while dict_line_count:
        current_count = min(dict_line_count.values())
        keys = list(dict_line_count.keys())
        index = list(dict_line_count.values()).index(current_count)
        name = keys[index]
        comb_to_file('comb_file.txt', name)
        comb_to_file('comb_file.txt', str(current_count))
        with open(name, 'r', encoding='utf-8') as f:
            text= list(f)
            comb_to_file('comb_file.txt', ''.join(text))
        dict_line_count.pop(name)


def comb_to_file(file, text):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(text + '\n')


counting_lines(['text_1.txt', 'text_2.txt', 'text_3.txt'])



