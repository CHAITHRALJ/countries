# This code will list all world countries with their TLD (top level domain).

# installation
pip install json

#usage
open command prompt, go to python and run the code by using python filename.py

# importing the packages

import json,requests 

# fuction to get the data
def getData(): 

# url which is containaing the information
  url = "https://restcountries.eu/rest/v2/all?fields=name;topLevelDomain" 
  
  # the data which is in JSON format
  header = {'content-type': 'application/json'} 
  
  # convert the json data to text format
  r = requests.get(url).text 
  
   # load that data to a variable
  data = json.loads(r)
  
  # for all the countries in data
  for country in data:  
  
  #printing all the tld for each country 
  print("{0}:{1}".format(country['name'],' '.join(country['topLevelDomain'])))
      
# returning the required output
getData() 



