from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
sw = stopwords.words('english')

def doc_preparer(doc, stem = False, stop_words=sw):
    '''
    :param doc: a document from the satire corpus 
    :return: a document string with words which have been 
            lemmatized, 
            parsed for stopwords, 
            made lowercase,
            and stripped of punctuation and numbers.
            
    Courtesy of Flatiron's lecture materials - 
    credit due to Daniel on helping me figure out the regex pattern to exclude Twitter mentions.
    '''

    
    # Instantiate regex tokenizer
    regex_pattern = r"(?<![@A-Za-z0-9_])([a-zA-Z]+(?:'[a-z]+)?)" 
    regex_token = RegexpTokenizer(regex_pattern)
    
    # Tokenize using regex pattern
    doc = regex_token.tokenize(doc)
    
    # Lowercase all letters
    doc = [word.lower() for word in doc]
    
    # Remove stop words
    doc = [word for word in doc if word not in sw]
   
    # Stemming
    if stem:
        p_stemmer = PorterStemmer()
        doc = [p_stemmer.stem(word) for word in doc]
        
    return ' '.join(doc)