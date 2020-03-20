from tkinter import filedialog as fd 


fname = fd.askopenfilename(filetypes = (("Text files", "*.txt"),("All file types", "*.*")))
print("the file you opened is:  " + fname)


#file_name = "script - Copy.txt"



string_to_add = "\\n{\\rDefault}"
fname_temp = fname
#file_name_out = fname_temp.strip('.txt')+ "_out.txt"


file_name_out = fname_temp.replace('.txt',"_out.txt")




new_lines = []
n = 1
with open(fname, 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if n % 2 !=0:    # line 1, 3, 5, so on
            new_lines.append(line.strip() + string_to_add)
        else:  # line 2, 4, 6, so on
            new_lines.append(line.strip()+'\n')
        n+=1

with open(file_name_out, 'w', encoding = 'utf-8') as fo:
    fo.writelines(new_lines) 
