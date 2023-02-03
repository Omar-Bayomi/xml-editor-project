"""
string Minify(string* XML_String)
{
	string M_string ="";
	for (unsigned int i = 0 ; i < XML_String->size() ; i++)
	{
		if(XML_String->at(i) == '\n')
			continue ;
		else if (XML_String->at(i) == ' ')
		{
			if((XML_String->at(i+1) >= 'A' && XML_String->at(i+1) <= 'Z' ) || ( XML_String->at(i+1) >= 'a' && XML_String->at(i+1) <= 'z' ) )
				M_string += XML_String->at(i) ;
		}
		else
			M_string += XML_String->at(i) ;
	}

	cout << "Saved :" << ( XML_String->size() - M_string.size() ) << " byte " << endl ;
	return M_string ;
}
"""

"""
    "Minify function 
    Time complexity     = O(n)
    space complexity    = O(n) 
"""
def Minify(XML_String):
    M_String = ""
    for i in range(len(XML_String)): #loop to search character by character in xml
        if XML_String[i] == '\n':    #if character equal '\n' so ignore it 
            continue
        elif XML_String[i] == ' ':  #if character equal ' ' so check the next character
            if ('A' <= XML_String[i + 1] <= 'Z') or ('a' <= XML_String[i + 1] <= 'z'): #if character equal to alphabet letters so add ' ' to M_String
                M_String = M_String + XML_String[i]
        else:
            M_String = M_String + XML_String[i] #otherwise add the character
    return M_String #return the string
"""
    "Formatting function" 
    Time complexity     = O(n)
    space complexity    = O(n) 
"""
def format_xml(XML_String):
    M_String = Minify(XML_String)       #call miniyfing funtion O(n)
    lvl = 0                             #Number of \t to be added 
    result = ""                    
    for i in range(len(M_String)):      #loop to search character by character in xml
        if M_String[i] == '<' and M_String[i+1] == '/':
            lvl -= 1
            result += (('\n' + ('\t' * lvl)) if result[-1] == '>' else '') + M_String[i]
        elif M_String[i] == '<':
            result += ("\n" if lvl > 0 else "") + ('\t' * lvl) + M_String[i]
            lvl += 1
        else:
            result += M_String[i]
    return result
