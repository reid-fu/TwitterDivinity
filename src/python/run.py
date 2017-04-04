import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

# Naive Bayes implementation
def classify_nb(train_data, train_labels, test_data, test_labels):
    # come up with word counts
    count_vect = CountVectorizer()
    x_train_counts = count_vect.fit_transform(train_data)
    
    # come up with frequencies using tf
    # EXPIREMENT test tf vs. tfidf
    tf_transformer = TfidfTransformer(use_idf=False).fit(x_train_counts)
    x_train_tf = tf_transformer.transform(x_train_counts)
    #tf_transformer = TfidfTransformer()
    #x_train_tf = tf_transformer.fit_transform(x_train_counts)
    
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


def classify_nn(train_data, train_labels, test_data, test_labels):
    print("")    
    

if __name__ == '__main__':
    # get data and split into train and test sets
    data_file = open("../../results/data")
    json_data = json.load(data_file)
    split_idx = int(len(json_data['tweets']) * 0.8)
    train_data = json_data['tweets'][:split_idx]
    train_labels = json_data['sentiment'][:split_idx]
    test_data = json_data['tweets'][split_idx+1:]
    test_labels = json_data['sentiment'][split_idx:]

    # test classifier with naive bayes
    classify_nb(train_data, train_labels, test_data, test_labels)
    classify_nn(train_data, train_labels, test_data, test_labels)
    
    
    
    
    
    
    
    
    
    
    
    
    