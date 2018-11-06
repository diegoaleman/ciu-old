# create list
l = [1, 'diego', 3.1415, 1993]

# update list
l[3] = 1994

# delete list element
# O(n)
del l[2]

# operations
size = len(l)       # O(1)
concat = [1,2,3] + [4,5,6]
mult = [1,2,3] * 3
memb = 3 in concat      # O(n)

# access elements from the back with negative index
last1 = l[len(l)-1]
last2 = l[-1]

# slice notation
# [start:end:step]
l2 = [1,2,3,4,5,6,7,8,9]
sl1 = l2[2:5]   # prints from index 2 to 4
sl2 = l2[0::2]  # ptints array from 0 to end with 2 step

# list of chars to a string
l3 = ['d','i','e','g','o']
list_to_string = ''.join(l3)

# list of integers to a string
l4 = [1,9,9,4]
list_to_number = ''.join(str(x) for x in l4)

# list to tuple and set
l5 = [1,2,3,4,5,6]
list_to_tuple = tuple(l5)
list_to_set = set(l5)

# list to dictionary
l6 = [1,'uno',2,'dos',3,'tres',4,'cuatro']
list_to_dict = dict(zip(l6[0::2], l6[1::2]))

# entend vs append
l7 = ['frog','lion','panda']
# extend takes an iterable and adds each element to the end of the list
l7.extend(['dog','bird'])
# append adds its argument to the end of the list as a SINGLE item
l7.append(['puma','bear'])

## pop
l7_last = l7.pop()      # O(1)
l7_first = l7.pop(0)    # O(n)

# sorted vs sort
# O(n log n)
l8 = [9,5,3,7,2,8,1]
# sorted returns a new list
sorted_l = sorted(l8)
# sort modifies the same list
l8.sort()
