hellofile = open('G:\\My Drive\\Learning\\Udemy\\Automate The Boring Stuff\\Hello.txt')
content = hellofile.read()
hellofile.close()

hellofilewrite = open('Hello2.txt', 'w')
hellofilewrite.write('Hello!!!!\n')
hellofilewrite.write('Hello!!!')
hellofilewrite.close()
hellofilewrite = open('Hello2.txt')
content2 = hellofilewrite.read()
print(content2)

import shelve

shelffile = shelve.open('mydata')
shelffile['Cats'] = ['Zophie', 'Pooka', 'Fat-Tail']
shelffile.close()
shelffile = shelve.open('mydata')
print(shelffile['Cats'])