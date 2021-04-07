#!/usr/bin/env python
# coding: utf-8

# In[186]:


from nltk import word_tokenize
from collections import Counter
import string
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

#Open StopWords file:
def open_stopwords(stopwords_file):
    stopfile = open(stopwords_file, "r")
    stopwordsls = []
    for line in stopfile:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        stopwordsls.append(line_list)
    stopwords = [item for sublist in stopwordsls for item in sublist ]
    return stopwords

# Open pro/con text file:
def open_file(file):
    file1 = open(file, "r")
    lst = []
    for lines in file1:
        stripped_line = lines.strip()
        line_list = stripped_line.split()
        lst.append(line_list)
    list_of_words = [item for sublist in lst for item in sublist]
    list_of_words = [x.lower() for x in list_of_words]
    return list_of_words

#Deleting the words present in stop words from Pro file:
def del_stopwords(list_of_words):
    n = len(list_of_words)
    for i in range(n - 1, -1, -1):
        if list_of_words[i] in stopwords:
            del list_of_words[i] 
    return list_of_words
        
#Considering only words greater than 3:
def del_less_3_words(list_of_words):
    list_of_words1=[]
    for i in list_of_words:
        if len(i)>3:
            list_of_words1.append(i)
    list_of_words = list_of_words1
    return list_of_words

#Removing Repeated words:
def remove_rep_words(list_of_words):
    list_of_words1 = []
    for i in list_of_words:
        if i not in list_of_words1:
            list_of_words1.append(i)
    return list_of_words1

#Removing punctuations:
def remove_punctuation(list_of_words):
    punctuations = list(string.punctuation)
    punctuations.append("''")
    list_of_words = [i.strip("".join(punctuations)) for i in list_of_words if i not in punctuations]
    return list_of_words
    
#Removing numbers and special symbols(COnsidering only a-z)
def remove_num_specialchar(list_of_words):
    list_of_words = [re.sub('[^a-zA-Z]+', '', _) for _ in list_of_words]
    return list_of_words

# Removing empty spaces from a file:
def remove_emptyspaces(list_of_words):
    while '' in list_of_words:
        list_of_words.remove('')  
    return list_of_words

# Joining bag of words into a list
def join_whole_text(list_of_words):
    list_of_words = ' '.join(list_of_words)
    return list_of_words

# Sentimental Analysis
def sentiment_analyzer_scores(list_of_words):
    score = analyser.polarity_scores(list_of_words)
    print(score)
    
    
def bigrams(list_of_words):
    bigrams = []
    for i in range(len(list_of_words)):
            try:
                bigrams.append(list_of_words[i] + "_" + list_of_words[i+1])  
            except:    
                pass 
    return bigrams


def main():
    open_stopwords("stopwords_en.txt")
    pro_list = open_file("pro.txt")
    con_list = open_file("con.txt")
    pro_list = del_stopwords(pro_list)
    con_list = del_stopwords(con_list)
    pro_list = del_less_3_words(pro_list)
    con_list = del_less_3_words(con_list)
    #Most 10 repeated words in pro:
    Most_pro_list = Counter(pro_list).most_common(10)
    print(f'Most repeated words in pro {Most_pro_list}')
    #Most 10 repeated words in con:
    Most_con_list = Counter(con_list).most_common(10)
    print(f'Most repeated words in con {Most_con_list}')
    pro_list = remove_rep_words(pro_list)
    con_list = remove_rep_words(con_list)
    pro_list = remove_punctuation(pro_list)
    con_list = remove_punctuation(con_list)
    pro_list = remove_num_specialchar(pro_list)
    con_list = remove_num_specialchar(con_list)
    pro_list = remove_emptyspaces(pro_list)
    con_list = remove_emptyspaces(con_list)
    pro_text = join_whole_text(pro_list)
    con_text = join_whole_text(con_list)
    sentiment_analyzer_scores(pro_text)
    sentiment_analyzer_scores(con_text)
    pro_bigrams =  bigrams(pro_list)
    con_bigrams = bigrams(con_list)
    Most_pro_bigrams_list = Counter(pro_bigrams).most_common(5)
    print(f'Mostly there are no repeated bigrams since repeated words are removed {Most_pro_bigrams_list}')
    #Most repeated words in con:
    Most_con_bigrams_list = Counter(con_bigrams).most_common(5)
    print(f'Mostly there are no repeated bigrams since repeated words are removed {Most_con_bigrams_list}')

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




