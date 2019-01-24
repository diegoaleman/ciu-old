# LAMBDA
# small, one-time, anonymous function objects
# one expression, any number of arguments
# lambda arguments : expression

add = lambda x,y : x+y
addition = add(2,3)



# MAP
# expects a function object and x num of iterables
# executed function for every element of iterable
# returns map object
# map(function_object, iterable1, iterable2, ...)

def multiply2(x):
    return x * 2
l1 = [1,2,3,4]
l2 = map(multiply2, l1)
print(list(l2))


l3 = map(lambda x: x*3, [1,2,3,4])
print(list(l3))


l_a = [1,2,3]
l_b = [10,20,30]
l_res = map(lambda x,y: x+y, l_a, l_b)
print(list(l_res))



# FILTER
# expects function and iterable
# function returns boolean
# function returns only true results of iterable elements
# only one iterable is permited
# filter(function_object, iterable)
# returns filter object

a = [1,2,3,4,5,6]
a_res = filter(lambda x:x%2==0, a)
print(list(a_res))



# ZIP
# takes n number of iterables and returns a list of tuples
# returns zip object

list_a = [1,2,3,4,5]
list_b = ['a','b','c','d','e']

zipped = zip(list_a, list_b)
zipped_l = list(zipped)
print(zipped_l)

# unzip list
unzip_a, unzip_b = zip(*zipped_l)
print(unzip_a)
print(unzip_b)

