import unicodedata

def compare_strings(search, title):
    
    a, b = 'áéíóúü','aeiouu'
    
    search =  remove_accents(search)
    title =  remove_accents(title)
    
    search =  search.lower()
    title =  title.lower()
    
    if search == title: return True
    else: return False


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii