
from underthesea import word_tokenize
import string
import pickle
import json
import os.path
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer 



def Talk_To_Bot(test_set_sentence):
    results = []
    if (test_set_sentence == "halo" or test_set_sentence == "hello" or test_set_sentence =="Xin chào" or test_set_sentence =="chào"):
        results.append("Hỏi gì hỏi đi!")
        return results
    json_file_path = "conversation_json.json" 
    tfidf_vectorizer_pickle_path =  "tfidf_vectorizer.pkl"
    tfidf_matrix_pickle_path = "tfidf_matrix_train.pkl"
    
    # ---------------Tokenisation of user input -----------------------------#
    tokens = RemovePunction(word_tokenize(test_set_sentence, format="text").split(' '))
    word_tokens = tokens
    
    filtered_sentence = []
    for w in word_tokens: 
        if w not in vietnamesestopword(): 
            filtered_sentence.append(w)  
    
    filtered_sentence =" ".join(filtered_sentence).lower()
            
    test_set = (filtered_sentence, "")

    
    #For Tracing, comment to remove from print.
    print("""USER'S INPUT AFTER FILTERING: """,filtered_sentence)
    
    # -----------------------------------------------------------------------#
        
    try: 
        # ---------------Use Pre-Train Model------------------#
        f = open(tfidf_vectorizer_pickle_path, 'rb')
        tfidf_vectorizer = pickle.load(f)
        f.close()
        
        f = open(tfidf_matrix_pickle_path, 'rb')
        tfidf_matrix_train = pickle.load(f)
        # ---------------------------------------------------#
    except: 
        print("something went wrong!!")
        # ------------------------------------------#
        
    #use the learnt dimension space to run TF-IDF on the query
    tfidf_matrix_test = tfidf_vectorizer.transform(test_set)
    print("tfidf shape:", np.shape(tfidf_matrix_test))
    #then run cosine similarity between the 2 tf-idfs
    cosine = cosine_similarity(tfidf_matrix_test, tfidf_matrix_train)

    req_tfidf = cosine.max()
    if (req_tfidf == 0): #Threshold A
        
        not_understood = "Xin lỗi, tôi không hiểu!"
        results.append(not_understood)
        return results
        
    else:
        Threshold_B = 0.1
        print("Shape of cosine matrix: ",np.shape(cosine))

        max = cosine.max()
        print("MAX SCORE:", max)
        response_index = 0
        #if max score is lower than < Threshold_B > (we see can ask if need to rephrase.)
        if (max <= Threshold_B): #Threshold B
            
            not_understood = "Xin lỗi, tôi không hiểu!"
            
            results.append(not_understood)
            return results
        else:

                #if score is more than Threshold_B list the multi response and get a random reply
                if (max > Threshold_B): #Threshold C
                    
                    # load them to a list
                    flatcosine = cosine.flatten()
                    listsuit = flatcosine.argsort()[-1:][::-1]
                    response_index = listsuit
                    print("best_indexes: ", response_index)
                # else:
                #     # else we would simply return the highest score
                #     response_index = np.where(cosine == max)[0][0] + 2 

              
                with open(json_file_path, "r", encoding='UTF8') as sentences_file:
                    reader = json.load(sentences_file)
                    rank = 0
                    for i in response_index:
                        j = 0 
                        for row in reader:
                            if ((j == i) and (flatcosine[i] >= Threshold_B)): 
                                rank += 1
                                # results.append(tuple((row["RESPONSE"], row["MESSAGE"], flatcosine[i])))
                                results.append(row["RESPONSE"] + "\nSCORE: "+ str(flatcosine[i]) )
                                print("\nTITLE: ", row["MESSAGE"], "\nRESPONSE: ", row["RESPONSE"], "\nSCORE: ",flatcosine[i])
                                print("\n")
                                break
                            j += 1 
                return results

def vietnamesestopword():
    with open("vietnamese-stopword.txt", "r", encoding='UTF8') as f:
        new_stopwords = []
        for line in f.readlines():
            new_stopwords.append(line[:-1])

    stop_words = new_stopwords[1:]
    return stop_words



def RemovePunction(tokens):
    return[t for t in tokens if t not in string.punctuation]



Talk_To_Bot("đất nước")