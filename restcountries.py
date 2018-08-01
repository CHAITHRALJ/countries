import json,requests

def getData():
    url="https://restcountries.eu/rest/v2/all?fields=name;topLevelDomain"
    header = {'content-type': 'application/json'}
    r = requests.get(url).text
    data = json.loads(r)
    count = 0
    for i in data:
        print("country name:")
        print(data[count]['name'])
        print("Top level Domain:")
        count1 = 0
        for j in data[count]['topLevelDomain']:
            print(data[count]['topLevelDomain'][count1])
            count1 = count1 + 1
        count = count + 1
        print("\n")
        
getData()

