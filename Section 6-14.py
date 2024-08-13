#for loop using the range function.
for i in range(4):
    print(i)

#for loop using a list.

for i in [0, 1, 2, 3]:
    print(i)

print(list(range(4)))
print(list(range(0, 100, 2)))

#a typical practice in python is to use the position in a list as an index for a for loop via the len function passed to range class
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#For assignements of the items within a list, you would tradionally each item in the list to a variable, like so
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

#here is how you do the multiple assignment "trick" in python
size, color, disposition = cat
print(size)
print(color)
print(disposition)

#Swap operations, lets say you want to swap the values of a and b
a = 'AAA'
b = 'BBB'
print(a + b)
a, b = b, a
print(a + b)

#augmented operators
spam = 42
#Typically...
spam = spam +1
#with a augmented operator...
spam += 1
print(spam)