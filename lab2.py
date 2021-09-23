import re
import profile


key_word = ['auto', 'break', 'case', 'char', 'const', 
            'continue', 'default', 'do','double', 'else', 'enum',
           'extern', 'float', 'for', 'goto', 'if','int', 'long',
          'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union', 
            'unsigned', 'void', 'volatile', 'while']                                            #All the keywords in C and C++ are generated here
file_name = input("Please input the file name:")
level = input("Please input the level(1-4):")                                                   #Determine the name of the object file and the processing level
level = int(level)
 
with open(file_name) as C_file:
    lines = C_file.readlines()
                                                                                                #open the object file and read it line by line
def Basic(lines):
    count = 0
    Key_words = []
    for line in lines:
            chars = ['(', ')', '{', '}', ':', ',', '<', '>', '=', '+', '-', '#', ';']
    
    for line in lines:
      
        line = re.sub(r'#.*$', "", line)
        line = re.sub(r'//.*',"",line)
        line = re.sub(r'".*"', "", line)
        line = re.sub(r"'.*'", "", line)
        
        if '/*' in line:
            first_line = lines.index(line)
            for new_line in lines[first_line:]:
                if '*/' not in new_line:
                    del lines[first_line]
                else:
                    del lines[first_line]
                    break
                                                                                                                                 
       
                                                                                                                                                                                                                                                      # Converts special characters to Spaces, word segmentation
        for ch in chars:
            line = line.replace(ch, ' ')
            word_line = line.split() 
        
        if 'else' in word_line and 'if' in word_line:                                                                         # Consider esle if as a whole to pave the way for the following function processing
            Key_words.append('elif')
            count += 2
        else:
            for word in word_line:
                if word in key_word:
                    count += 1
                    Key_words.append(word)
    return Key_words, count

def Advanced(Key_words):
   
    case_num = []
    structure_num = 0  
    while True:
        num = 0
        if 'default' in Key_words:
            subscript = Key_words.index('default')
            structure_num += 1                                                               # The number of SwitchCase structures is identified by the number of default    
            for word in Key_words[:subscript]:
                if word == 'case':
                    num += 1
            case_num.append(num)                                                              #dentify the number of cases in each group
            del Key_words[:subscript + 1]
        else:
            break
    return case_num, structure_num

def  Ultimate(Key_words):
   
    if_num = 0
    list = []
    if_elif_num = 0
    for word in Key_words:
        count = 0                                                        

        if word == 'if':
            if_num += 1

        if word == 'if' or word == 'elif':
            list.append(word)
        elif word == 'else':
            while True:
                temp = list.pop()
                if temp == 'elif':
                    count = 1
                elif temp == 'if':
                    break
        if count == 1:
            if_elif_num += 1


    for word in list:                                                                           # Consider that there is no else in if else if structure
        if word == 'if':
            if_num -= 1
    return if_num, if_elif_num

       
 
            


                                                                                               # Call and execute the function

def fun():
    Key_words, total_num = Basic(lines)
    case_nums , switch_nums = Advanced(Key_words[:])
    if_nums, if_elif_nums =  Ultimate(Key_words[:])
    if level >= 1:
        print(f"total num:{total_num}")
    if level >= 2:
        print(f"switch num:{switch_nums}")
        print("case num:", end = ' ')
    for case in case_nums:
        print(case, end = ' ')

    if level >= 3:
    
        print('\n'f"if-else num:{if_nums - if_elif_nums}")
    if level >= 4:
    
        print(f"if-elif_num:{if_elif_nums}")

    return 0

profile.run('fun()')
