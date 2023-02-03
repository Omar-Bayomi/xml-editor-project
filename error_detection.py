
class tag:
    def __init__(self, name = 'none', line_num = 0):
        self.name = name
        self.line_num = line_num

"""
    "error_check" 
    Time complexity     = O(n)
    space complexity    = O(n) 
"""
# opening the text file
def error_check(xml_file):
    with open(xml_file, 'r') as file:
        tags_stack = []
        tags_redundant_stack = []
        line_count = 0
        # reading each line
        Extra_flag = False
        error = False



        for line in file:
            if Extra_flag == True: 
                print('error: extra content are added after the end of root tag')
                error = True
                break
            line_count += 1
            for word in line.split():
                    tag_name = ''
                    tag_ready = False
                    opening = False
                    closing = False

                    for character in word:
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

                        if (not tag_ready) and (opening or closing): # completing tag word
                            tag_name = tag_name + character

                        elif tag_ready and (opening or closing): # process the tag after completing
                            if Extra_flag == True:
                                break
                            tag_obj = tag()
                        
                            tag_obj.name = tag_name.replace('<', '').replace('/', '').replace('>', '') # tag_name is word with no brackets
                            
                            tag_obj.line_num = line_count
                            # check if the word is a tag or not
                        
                            
                            if opening == True:
                                    tags_stack.append(tag_obj)
                                    tags_redundant_stack.append(tag_obj)
                                    
                            
                            else :  
                                    # check if the closing was preceded with an opening
                                    # always pop from redundant stack
                                    if len(tags_redundant_stack) != 0:
                                        tags_redundant_stack.pop()
                                        if tags_stack[-1].name == tag_obj.name :
                                            tags_stack.pop()
                                            if len(tags_stack) == 0:
                                                Extra_flag = True ## this means that all the coming tags are extra, so no need to proccess them
                                                
                                        else:

                                            # print error clause
                                            print('error using wrong closing \'</{}>\' at line {}, should be \'</{}>\''.format(
                                                                                                                tag_obj.name, line_count , tags_stack[-1].name))
                                            error = True
                        
                            opening = closing = False    
                            tag_name = '' 



                        # use opeing or closing to compare stack top with added one then they are set to false to distinguish between 
                        # letters after < and normal letters in words
                        
                        else: # some character out of tags
                            pass



            
        # check stack is null or not at the end of file
        if len(tags_stack) != 0:
            # print error having open with no closing
            # any opening that has no closing
            while len(tags_redundant_stack) != 0:
                print('error: opening without closing \'<{}>\' at line {}'.format(tags_redundant_stack[-1].name,
                                                                                     tags_redundant_stack[-1].line_num))
                error = True                                                                     
                tags_redundant_stack.pop()

        elif error == False: # no error
            print("checked successfully: no errors")        
            

                
"""
    "error_correction function"
    Time complexity     = O(n)
    space complexity    = O(n) 
"""
