import json
filenames = ['data1', 'data2', 'data3', 'data4', 'data5', 'data6', 'data7']
data = {}
data['tweets'] = []
data['sentiment'] = []
for fn in filenames:
    file = open(fn)
    json_data = json.load(file)
    
    data['tweets'].extend(json_data['tweets'])
    data['sentiment'].extend(json_data['sentiment'])
    file.close()

with open('data', 'w') as outfile:  
    json.dump(data, outfile)
