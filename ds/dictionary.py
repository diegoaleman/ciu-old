# create dict
d1 = {'name': 'diego', 'last_name':'aleman', 'age':24, 'random':'blabla'}

k = ['a','b','c']
v = [1,2,3]
list_to_dict = dict(zip(k,v))

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



# Chain Maps
# manage multiple dicts as one unit
# eliminates duplicate keys
# main use is to search multiple dicts at the same time
import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

dict_keys = list(res.keys())
dict_values = list(res.values())

for key,val in res.items():
    print(key + "-" + val)

value_in_dict_1 = 'day1' in res
value_in_dict_2 = 'day5' in res

res['day3'] = 'Fri'
res['day1'] = 'Sat'
dict1['day2'] = 'Sun'

print(res.maps, '\n')

