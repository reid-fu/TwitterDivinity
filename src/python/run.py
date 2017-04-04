import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

import nltk
from nltk.stem.lancaster import LancasterStemmer

# Naive Bayes implementation
def classify_nb(train_data, train_labels, test_data, test_labels):
    # come up with word counts
    count_vect = CountVectorizer()
    x_train_counts = count_vect.fit_transform(train_data)
    
    # come up with frequencies using tfidf
    tf_transformer = TfidfTransformer()
    x_train_tf = tf_transformer.fit_transform(x_train_counts)
    
    # train naive bayes
    clf = MultinomialNB().fit(x_train_tf, train_labels)
    
    # get test data
    x_new_counts = count_vect.transform(test_data)
    x_new_tf = tf_transformer.transform(x_new_counts)
    
    # classify
    predicted = clf.predict(x_new_tf)
    correct = 0
    for doc, category, actual_category in zip(test_data, predicted, test_labels):
        print("%r => %s (%s)\n" % (doc, category, actual_category))
        if category == actual_category:
            correct += 1
    print("Correct: %d/%d" % (correct, len(predicted)))


# Neural network implementation
def classify_nn(data, labels):
    # stem/count words
    words = []
    docs = []
    for t, l in zip(data, labels):
        w = nltk.word_tokenize(t)
        words.extend(w)
        docs.append((w, l))
    stemmer = LancasterStemmer()
    words = [stemmer.stem(w.lower()) for w in words if "//t.co/" not in w] # remove urls
    words = list(set(words))
        
    # bag of words for each sentence
    training_vectors = []
    for d in docs:
        bag = []
        doc_words = d[0]
        doc_words = [stemmer.stem(w.lower()) for w in doc_words]
        for w in words:
            bag.append(int(w in doc_words))
        training_vectors.append(bag)
    
    print(training_vectors[0])
    
    # split into test/train data sets
    split_idx = int(len(data) * 0.8)
    train_data = data[:split_idx]
    train_labels = labels[:split_idx]
    test_data = data[split_idx+1:]
    test_labels = labels[split_idx:]
    
    
    
    

if __name__ == '__main__':
    # get data and split into train and test sets
    data_file = open("../../results/data")
    json_data = json.load(data_file)
    split_idx = int(len(json_data['tweets']) * 0.8)
    train_data = json_data['tweets'][:split_idx]
    train_labels = json_data['sentiment'][:split_idx]
    test_data = json_data['tweets'][split_idx+1:]
    test_labels = json_data['sentiment'][split_idx:]

    # test naive bayes and neurral network
    #classify_nb(train_data, train_labels, test_data, test_labels)
    classify_nn(json_data['tweets'], json_data['sentiment'])
    
