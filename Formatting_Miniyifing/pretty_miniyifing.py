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
    for i in range(len(XML_String)):
        if XML_String[i] == '\n':
            continue
        elif XML_String[i] == ' ':
            if ('A' <= XML_String[i + 1] <= 'Z') or ('a' <= XML_String[i + 1] <= 'z'):
                M_String = M_String + XML_String[i]
        else:
            M_String = M_String + XML_String[i]
    return M_String
"""
    "Formatting function" 
    Time complexity     = O(n)
    space complexity    = O(n) 
"""
def format_xml(XML_String):
    M_String = Minify(XML_String)
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
    return result
