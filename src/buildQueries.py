import re

'''probably build inverse index via MapReduce later
'''

def process_files(filenames):
    '''
        1. use 'with' later
        2. understand the pattern
    '''
    file_to_terms = {}
    p = re.compile('[\W_]+')
    for filename in filenames:
        f = open(filename, 'r')
        doc = f.read().lower()
        doc = pattern.sub(' ', doc)
        re.sub(r'[\W_]+', '', doc)
        file_to_terms[f] = doc.split()
        f.close()
    return file_to_terms
        
