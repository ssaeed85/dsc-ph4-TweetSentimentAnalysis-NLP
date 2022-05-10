from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
sw = stopwords.words('english')

def doc_preparer(doc, stem = False, stop_words=sw):
    '''
    doc: a text document from the corpus 
    stop_words: stopwords. defaults to nltk's stopwords
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
    doc = [word for word in doc if word not in stop_words]
   
    # Stemming
    if stem:
        p_stemmer = PorterStemmer()
        doc = [p_stemmer.stem(word) for word in doc]
        
    return ' '.join(doc)

def getTopWordFreq(df,col,n,stop_words):
    '''
    generates FreqDist and prints out top n words
    df: dataframe
    col: column you want to run a freqDist on
    n: number of most common items 
    stop_words: stopwords. defaults to nltk's stopwords
    '''
    word_freq = FreqDist()
    for text in df[col].map(lambda x:doc_preparer(x,stem=False,stop_words=stop_words)):
        for word in text.split():
            word_freq[word] +=1
    return word_freq.most_common(n=n)