def create_ascii(coords):
    
    equivalents = {-1:'.',0:')',1:'!',2:'@',
                    3:'#',4:'$',5:'%',6:'^',7:'&',
                    8:'*',9:'(',10:';',11:':',12:'/',
                    13:'\\',14:'|',16:'<',18:'>',27:'+'}
    
    string_ascii = ""
    for arr in coords:
        for val in arr:
            string_ascii+=equivalents[val]   
        string_ascii+='\n'
        
    return string_ascii