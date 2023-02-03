import os



def Minify(path):
    filename, file_extension = os.path.splitext(path)
    output_path = filename + 'minified.txt'
    with open(path, 'r+') as file, open(output_path, 'w') as output:
        XML_String = file.read()
        
        M_String = ""
        for i in range(len(XML_String)):
            if XML_String[i] == '\n':
                continue
            elif XML_String[i] == ' ':
                if ('A' <= XML_String[i + 1] <= 'Z') or ('a' <= XML_String[i + 1] <= 'z'):
                    M_String = M_String + XML_String[i]
            else:
                M_String = M_String + XML_String[i]
    
        output.write(M_String) 
   
    return output_path
