

# Python program to read
# file word by word
class tag:
    def __init__(self, name = 'none', line_num = 0):
        self.name = name
        self.line_num = line_num

# opening the text file
def error_check(xml_file = 'tst.txt'):
    with open(xml_file, 'r') as file:
        tags_stack = []
        tags_redundant_stack = []
        line_count = 0
        # reading each line



        for line in file:
            line_count += 1
            # reading each word
            for word in line.split():

                # displaying the words
                tag_obj = tag()
                tag_obj.name = word.replace('<', '').replace('/', '').replace('>', '') # tag_name is word with no brackets
                tag_obj.line_num = line_count
                # check if the word is a tag or not
                if word[0] == '<':
                    # chech if the word is an opening or closing tage
                    if word[1] == '/':
                        # check if the closing was preceded with an opening
                        # always pop from redundant stack
                        tags_redundant_stack.pop()
                        if tags_stack[-1].name == tag_obj.name:
                            tags_stack.pop()
                        else:

                            # print error clause
                            print('error using wrong closing \'{}\' at line {}'.format(word, line_count))

                    else:
                        tags_stack.append(tag_obj)
                        tags_redundant_stack.append(tag_obj)

        # check stack is null or not at the end of file
        if len(tags_stack) != 0:
            # print error having open with no closing
            # any opening that has no closing
            while len(tags_redundant_stack) != 0:
                print('error: opening without closing \'<{}>\' at line {}'.format(tags_redundant_stack[-1].name,
                                                                                     tags_redundant_stack[-1].line_num))
                tags_redundant_stack.pop()

