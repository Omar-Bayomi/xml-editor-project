

def error_correction(xml_file ):
    
    with open(xml_file, 'r') as file:
        tags_stack = []
        tags_redundant_stack = []
        line_count = 0
        # reading each line
        Extra_flag = False
        Extra_correction_flag = False
        error = False
        content = ' '



        for line in file:
            if Extra_correction_flag == True: 
                error = True
                break
            line_count += 1
            for word in line.split():
                    if Extra_correction_flag == True: 
                        break
                    tag_name = ''
                    word_buffer = ''
                    tag_ready = False
                    opening = False
                    closing = False

                    for character in word:
                        if Extra_correction_flag == True: 
                            break
                        if character == '<' :
                            opening = True
                            tag_ready = False

                        elif character == '/' :
                            closing = True
                            opening = False
                            tag_ready = False

                        elif character == '>' :
                            tag_ready = True
                               
                
                        else:
                            tag_ready = False

                        if (not tag_ready) and (opening or closing):
                            tag_name = tag_name + character

                        elif tag_ready and (opening or closing): # process the tag
                            if Extra_flag == True:
                                break
                            tag_obj = tag()
                        
                            tag_obj.name = tag_name.replace('<', '').replace('/', '').replace('>', '') # tag_name is word with no brackets
                            
                            tag_obj.line_num = line_count
                            # check if the word is a tag or not
                        
                            
                            if opening == True:
                                    tags_stack.append(tag_obj)
                                    tags_redundant_stack.append(tag_obj)
                                    content = content + tag_name + '>' 
                            
                            else :  
                                    # check if the closing was preceded with an opening
                                    # always pop from redundant stack
                                    if len(tags_redundant_stack) != 0:
                                        tags_redundant_stack.pop()
                                        if tags_stack[-1].name == tag_obj.name :
                                            tags_stack.pop()
                                            
                                            content = content + '</' + tag_obj.name + '>'
                                            if len(tags_stack) == 0:
                                                Extra_correction_flag = True ## this means that all the coming tags are extra, so no need to proccess them'''
                                                
                                                
                                        else:

                                            # change error closeing with true one
                                            content = content + '</' + tags_stack[-1].name + '>'
                                            tags_stack.pop()
                                            error = True
                        
                            opening = closing = False   # after tag proccessing, change flags and reset tag_name 
                            tag_name = '' 



                        # use opeing or closing to compare stack top with added one then they are set to false to distinguish between 
                        # letters after < and normal letters in words
                        
                        #in case opening bracket is missed
                        elif tag_ready == True and not opening and not closing:
                            tag_obj = tag()
                            tag_obj.name = word_buffer.replace('<', '').replace('/', '').replace('>', '')
                            tag_obj.line_num = line_count
                            tags_stack.append(tag_obj)
                            tags_redundant_stack.append(tag_obj)
                            content = content.rsplit(' ', 1)[0] + '<' + word_buffer + '>'



                        else: # some character out of tags
                            content = content + character
                            word_buffer = word_buffer + character # used in case '>' is used at the end of a word
                
                    content = content + ' ' # add space after each word

        
        # check stack is null or not at the end of file
        if len(tags_stack) != 0:
            # try to correct the error
            # any opening with no closing
            while len(tags_redundant_stack) != 0:
                content = content + ' </' + tags_redundant_stack[-1].name + '>'
                tags_redundant_stack.pop()

        print(content)
        return content        

                            


# call both functions
#error_correction('tst5.txt')
print(format_xml(error_correction('tst3.txt').strip()))

