import json
import random
from model.utils import *
from nltk.corpus import stopwords
import numpy as np
from model.NBModel import brain


def main():
    df = loadDataset()
    Topics, all_words, Xy = [],[],[]
       
    #get the data from dataset
    for data in df['data']:
       topic = data['topic']
       Topics.append(topic)
       for Q in data['questions']:
           tokens = tokenizer(Q)
           all_words.extend(tokens)
           Xy.append( (tokens,topic) )

    #clean the text
    all_words = clean_text(all_words)
    #sorte the set of words
    all_words = sorted(set(all_words))
    #sorte the set of topics
    Topics = sorted(set(Topics))
    #split the dataset to X and y
    X,y = bag_of_words(Xy,Topics,all_words)
    #create the model
    model = brain(X,y)
    #train the model
    model.train()
    
    return df,Topics,all_words,model


def loadDataset():
    with open('model/dataset/MyChatbotDataset.json','r') as f:
        df = json.load(f)
    return df


def bag_of_words(Xy,Topics,all_words):
    X = []
    y = []

    for (tokens,topic) in Xy:
        bag = bagOfWords(tokens,all_words)
        X.append(bag)
        label = Topics.index(topic)
        y.append(label)
    
    X = np.array(X)
    y = np.array(y)
    return X,y

def test_model(all_words,message,model):
    tokenized_sentence = tokenizer(message)
    X = np.array(bagOfWords(tokenized_sentence,all_words))
   
    index = model.test(X)
    return index

def getAnswer(df,Topics,index):
    for data in df['data']:
       if data['topic'] == Topics[index]:
          return random.choice(data['answers'])
            
def user_input(df,Topics,all_words,message,model):
    index = test_model(all_words,message,model)
    answer = getAnswer(df,Topics,index)
    return answer
