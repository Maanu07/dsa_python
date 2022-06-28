#Sort Python Dictionaries by Key or Value
""" dict = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}
for i in sorted(dict.keys()):
  print(i,dict[i]) """


#Handling missing keys in Python dictionaries
#method 1 => using get(key,default_value) method

""" country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
print(country_code.get('Russia','Not found'))
print(country_code.get('India','Not found'))
print(len(country_code)) """

#Find the size of a Dictionary in Python
""" import sys 
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
print(str(sys.getsizeof(dic3)) + ' bytes') """
