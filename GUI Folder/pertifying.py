
import os
def prettyfing(path):
    
    filename, file_extension = os.path.splitext(path)
    output_path = filename + '_pretty'+'.txt'
    with open(path, 'r+') as file, open(output_path, 'w') as output:
        M_String = file.read()

        
        lvl = 0
        result = ""
        for i in range(len(M_String)):
            if M_String[i] == '<' and M_String[i+1] == '/':
                lvl -= 1
                result += (('\n' + ('\t' * lvl)) if result[-1] == '>' else '') + M_String[i]
            elif M_String[i] == '<':
                result += ("\n" if lvl > 0 else "") + ('\t' * lvl) + M_String[i]
                lvl += 1
            else:
                result += M_String[i]
        
        output.write(result)  
              
    return result