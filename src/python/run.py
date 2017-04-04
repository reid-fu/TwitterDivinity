import json
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

# Naive Bayes implementation
def classify_nb(data):
    # partition data into test and train data sets
    # EXPERIMENT with different splits
    split_idx = int(len(data.tweets) * 0.2) # 20%
    train_tweets = data.tweets[:split_idx]
    train_labels = data.labels[:split_idx]
    test_tweets = data.tweets[split_idx:]
    test_labels = data.labels[split_idx:]
    
     # get training data
    categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
    train = fetch_20newsgroups(subset='train', categories = categories, shuffle=True, random_state=42)
    
    # come up with word counts
    count_vect = CountVectorizer()
    x_train_counts = count_vect.fit_transform(train_tweets)
    
    # come up with frequencies using tf
    # EXPIREMENT test tf vs. tfidf
    tf_transformer = TfidfTransformer(use_idf=False).fit(x_train_counts)
    x_train_tf = tf_transformer.transform(x_train_counts)
    
    # train naive bayes
    clf = MultinomialNB().fit(x_train_tf, train_labels)
    
    # get test data
    x_new_counts = count_vect.transform(test_tweets)
    x_new_tf = tf_transformer.transform(x_new_counts)
    
    # classify
    predicted = clf.predict(x_new_tf)
    for doc, category in zip(test_tweets, predicted):
        print("%r => %s" % (doc, train.target_names[category]))


if __name__ == '__main__':
    data_file = open("data_set")
    
    json_data = json.load(data_file)
    count_vect = CountVectorizer()
    count_map = count_vect.fit_transform(json_data.data)
    
    # test classifier with naive bayes
    classify_nb(json_data.data)
    
    