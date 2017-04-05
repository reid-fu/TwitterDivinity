import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier
import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer

# Naive Bayes implementation
def classify_nb(train_data, train_labels, test_data):
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
    return clf.predict(x_new_tf)

# Neural network implementation
def classify_nn(data, labels):    
    # create corpus of stemmed words
    words = []
    docs = []
    for t, l in zip(data, labels):
        w = nltk.word_tokenize(t)
        words.extend(w)
        docs.append(w)
    stemmer = LancasterStemmer()
    words = [stemmer.stem(w.lower()) for w in words if "//t.co/" not in w] # remove urls
    words = list(set(words))
    # bag of words for each tweet
    input_vectors = []
    for d in docs:
        bag = []
        doc_words = [stemmer.stem(w.lower()) for w in d]
        for w in words:
            bag.append(int(w in doc_words))
        input_vectors.append(bag)
    # split into test/train data sets
    split_idx = int(len(data) * 0.8)
    train_data = input_vectors[:split_idx]
    train_labels = labels[:split_idx]
    test_data = input_vectors[split_idx:]
    test_labels = labels[split_idx:]
    test_text = data[split_idx:]
    # train MLP
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,  activation='logistic',
                        hidden_layer_sizes=(25,), random_state=1) # best: (20,)
    clf.fit(train_data, train_labels)
    return clf.predict(test_data)
        
def calc_accuracy(expected_labels, actual_labels, text=None, bprint=False):
    if bprint:
        for tweet, exp_label, act_label in zip(text, actual_labels, expected_labels):
            print("%d (%d): %s\n" % (act_label, exp_label, tweet))
    correct = np.equal(expected_labels, actual_labels)
    return sum(correct)/float(len(expected_labels))

if __name__ == '__main__':
    # get data and split into train and test sets
    data_file = open("../../results/data")
    json_data = json.load(data_file)
    data_file.close()
    split_idx = int(len(json_data['tweets']) * 0.8)
    train_data = json_data['tweets'][:split_idx]
    train_labels = json_data['sentiment'][:split_idx]
    test_data = json_data['tweets'][split_idx:]
    test_labels = json_data['sentiment'][split_idx:]

    # test naive bayes and neurral network
    predicted1 = classify_nb(train_data, train_labels, test_data)
    predicted2 = classify_nn(json_data['tweets'], json_data['sentiment'])
    
    # calculate accuracy
    acc1 = calc_accuracy(test_labels, predicted1)
    acc2 = calc_accuracy(test_labels, predicted2)
    print("NB Accuracy: " + str(acc1))
    print("NN Accuracy: " + str(acc2))