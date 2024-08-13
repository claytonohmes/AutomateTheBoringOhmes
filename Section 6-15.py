spam = ['Hello', 'Howdy', 'Hi', 'Heyas']
#the index method returns the index or the position
print(spam.index('Hello'))
print(spam.index('Heyas'))
#print(spam.index('yo')) this will raise an exeception because this value is not in the list

spam = ['cat', 'dog', 'cat', 'mouse']
print(spam.index('cat'))
#the append method will add a value to the end of the list.
spam.append('Horse')
print(spam)
spam.insert(1,'chicken')
print(spam)
spam.remove('Horse')
print(spam)

spam.sort()
#this works with letters or numbers
print(spam)
#it also with the reverse argument passed
spam.sort(reverse=True)
print(spam)

spam = ['a', 'Z','b', 'C']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)
