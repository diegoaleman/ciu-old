# create dict
d1 = {'name': 'diego', 'last_name':'aleman', 'age':24, 'random':'blabla'}

# access dict
d_value = d1['name']

# access non existent key
#d_val_non1 = d1['non_existent']    # returns ERROR
d_val_non2 = d1.get('non_existent') # returns None

# updating dict
d1['name'] = 'maria'

# delete element
del d1['random']

# pop - retrieve and remove key:value from dict
d2 = {'brand':'nike', 'time':'twelve'}
brand = d2.pop('brand')

# keys & values
keys = d1.keys()
values = d1.values()

# items - return tuple with key:value pairs
items = list(d1.items())    # has to be casted to list, returns view not list
first_pair = items[0]
