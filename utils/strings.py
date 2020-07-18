def compare_strings(search, tittle):
    a, b = 'áéíóúü','aeiouu'
    
    search =  search.maketrans(a, b).replace(' ','')
    tittle =  tittle.maketrans(a, b).replace(' ','')
    
    if search == tittle: return True
    else: return False
        