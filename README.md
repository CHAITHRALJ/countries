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
  
  # assign a country name to a variable called string 
  string= country['name'] + ': '
  
  # for all tld in each countries 
   for tld in country['topLevelDomain']: 
   
   #cancatenating country name with tld
      string+= tld + ' '
      print( string"\n")
      
# returning the required output
getData() 



