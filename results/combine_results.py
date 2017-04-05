import json
filenames = ['data', 'data_1', 'data_2', 'data_3', 'data_4', 'data_5', 'data_6', 'data_7', 'data_8']
data = {}
data['tweets'] = []
data['sentiment'] = []
for fn in filenames:
    file = open(fn)
    json_data = json.load(file)
    
    data['tweets'].extend(json_data['tweets'])
    data['sentiment'].extend(json_data['sentiment'])
    file.close()

with open('data_final', 'w') as outfile:  
    json.dump(data, outfile)
