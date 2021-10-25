from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import numpy as np
import re

#create instance of PorterStemmer class
stemmer = PorterStemmer()
stopWords = stopwords.words('english')
stopWords.remove('not') 

def tokenizer(text):
    return word_tokenize(text)


def stem(tokenized_text):
    return stemmer.stem(tokenized_text.lower())


def bagOfWords(tokenized_sentence,all_words):
    #initite the bag of words!
    tokenized_sentence = clean_text(tokenized_sentence)
    #initiate the bag with zeros for first time!
    bag = np.zeros(len(all_words),dtype=np.float32)
    for i in range(len(all_words)):
    
        if all_words[i] in tokenized_sentence:
            bag[i] = 1.0
    
    return bag


def clean_text(all_words):
    #set the rule to detct the word!
    rgx = re.compile('[A-z]+')
    char = []#store all chars here to be removed in next step!
    for i in range(len(all_words)):
        #check if it word or char?
        if(rgx.match(all_words[i]) != None):
            if all_words[i] not in stopWords:
                all_words[i] = stem(all_words[i])
        else:
           char.append(all_words[i])
    #remove the chars
    for ch in char:
        all_words.remove(ch)

    return all_words