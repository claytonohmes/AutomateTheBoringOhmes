spam = [5, 6, 7, 'cat'] #spam is now a list data type

print(spam[0]) #the first index in the list starts with 0
print(spam[1])
print(spam[2])
print(spam[3])

ham = [['cat', 'bat'], [10, 20, 30, 40, 50]]

print(ham[0])
print(ham[0][1])
print(ham[1][0])
print(ham[1][1])
print(ham[-1])
print(ham[-1][-2])

spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[1:3]) # this is a slice, it will output a new list.

#assign new valus to a list by changing an indexed variable.
eggs = [3, 6, 9, 12, 15]
print(eggs)
eggs[3] = 'Damn '
eggs[4] = 'She Fine.'
print(eggs)

#assign new values to lists using slices
eggs = [3, 6, 9, 12, 15]
print(eggs)
eggs[3:5] = ['Damn ', 'She fine.'] #you can assing new lists to a list with a slicer.
print(eggs)
eggs[3:7] = ['Damn ', 'She fine.', 'Get', 'Low'] #additionally you can use a slicer to expand a list.
print(eggs)

#Slice shortcuts
eggs = [3, 6, 9, 12, 15]
print(eggs[:2])
print(eggs[2:])

#deleting items from a list. Use the del function.
eggs = [3, 6, 9, 12, 15]
del eggs[3]
print(eggs)

#use the len function to print the number of items in a list.
eggs = [3, 6, 9, 12, 15]
print(len(eggs))

#The same way you can do string concatination, you can do list concat.
sam = [1, 2, 3]
iAm = [4, 5, 6]
print(sam + iAm)
#The same way you can replicate a string, you can replicate a list.
print(sam * 3)

#The list function will return a list version of any value you pass it, for example
print(list('hello'))

#the in operator. returns true if the value is in the list.
eggs = [3, 6, 9, 12, 15]
print(6 in eggs)
print(7 in eggs)
print(7 not in eggs)
print(6 not in eggs)