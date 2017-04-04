from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

# get training data
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
train = fetch_20newsgroups(subset='train', categories = categories, shuffle=True, random_state=42)

# come up with word counts
count_vect = CountVectorizer()
x_train_counts =count_vect.fit_transform(train.data)

# come up with frequencies using tf-idf
tfidf_transformer = TfidfTransformer(use_idf=False).fit(x_train_counts)
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
print(x_train_tfidf.shape)

# train naive bayes
clf = MultinomialNB().fit(x_train_tfidf, train.target)

# get test data
docs_new = ['God is love', 'OpenGL on the GPU is fast']
x_new_counts = count_vect.transform(docs_new)
x_new_tfidf = tfidf_transformer.transform(x_new_counts)

# classify
predicted = clf.predict(x_new_tfidf)
for doc, category in zip(docs_new, predicted):
    print("%r => %s" % (doc, train.target_names[category]))

