import json,requests  # importing the packages

def getData():  # fuction to get the data
  url = "https://restcountries.eu/rest/v2/all?fields=name;topLevelDomain"  # url which is containaing the information
  header = {'content-type': 'application/json'}  # the data which is in JSON format
  r = requests.get(url).text  # convert the json data to text format
  data = json.loads(r)  # loads the data to a variable
  for country in data:   # for all the countries in data
    for country in data:
      print("{0}:{1}".format(country['name'],' '.join(country['topLevelDomain'])))        
getData()   # returning the required output


