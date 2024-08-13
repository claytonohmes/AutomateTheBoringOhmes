name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('Done')

password = 'swordfish'
if password == 'swordfis':
    print('Access Granted')
else:
    print('Wrong Password')

name = 'Bob' #executes the first true 
#statement then skips the rest.
age = 1500
if name == 'ALice':
    print('Hi ALice')
elif age < 12:
    print('YOu are not allice, kiddo')
elif age > 2000:
    print('you are old')
elif age > 100:
    print('You are not alice granny')

# Truthy and falsey values. Blank strings are falsey
print('enter a name')
name = input()
if name:
    print('thank you for entering')
else:
    print('you didnt enter')