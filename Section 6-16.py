import copy

name = 'Zophie'
print(name[0])
print(name[-2])
print('Zo' in name)
print('xxx' in name)

name1 = 'Zophie a cat'
#use the indexes in the string up to the desired point of replacement then concatonate.
NewName = name1[0:7] + 'the' + name1[8:12]
print(NewName)

#This part makes sense here
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
#cheese[1] = 'Hello!'
print(cheese)
#here is what is weird
print(spam)

def eggs(SomeParametr):
    SomeParametr.append('Hello')

eggs(spam)
print(spam)
#just screwing around below
#def plusone(number):
 #   number += 1
  #  return number

#print(plusone(5))

wine = copy.deepcopy(spam)
wine[0] = 5
print(wine)
print(spam)

#line continuation

indentedlist = ['apple',
                'oranges',
                'bananas',
                'cats']

print('When I was a young boy my' + \
      ' father took me into the city')