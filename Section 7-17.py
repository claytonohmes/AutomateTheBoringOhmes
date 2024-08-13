myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
#the items to the left of the collen are the key and the items to the right
#are it's value.
print(myCat['size'])

print('my cat has ' + myCat['color'] + ' Fur.')

eggs = {'name': 'Muji', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Muji', 'age': 8}
print(eggs == ham)

#you can use the following methods to list out the properties of keys
print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

#you can also use for loops to list the keys or values in a dictionary
for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

#additionally you can use multiple assignment as below.
for k, v in eggs.items():
    print(k, v)

print('cat' in eggs.values())

#to avoid a key error, you want to check if the value or key is in
#a dictionary, this if statement is a cumbersome way to do so.
if 'color' in eggs:
    print(eggs['color'])

#you can use 2 arguments for the get method in a dictonary
#first, what key to return the values of if it exists, and
# second what to return if it does not.
print(eggs.get('age', 0))
print(eggs.get('color', ''))

#quick example
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) \
      + ' to the picnic')

#using the set default method.
#here is the code you would have to implement if you did not \
#have this method

#if 'color' not in eggs:
#    eggs['color', 'black']
eggs.setdefault('color', 'black')
print(eggs)
#using the set default method again will not change the value.
eggs.setdefault('color', 'oragne')
print(eggs)
