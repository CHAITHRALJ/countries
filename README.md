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
  
   # load that data to a vriable
  data = json.loads(r)
  
  # for all the countries in data
  for country in data:   
  
 # prints the all toplevel domain of the country
   
   for tld in country['topLevelDomain']: 
      print(country['name'], end='')
      print (',',tld)
      print("\n")
      
# returning the required output
getData() 



