import json
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == '__main__':
    data_file = open("data_set")
    json_data = json.load(data_file)
    count_vect = CountVectorizer()
    count_map = count_vect.fit_transform(json_data.data)