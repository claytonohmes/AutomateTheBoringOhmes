import os
import send2trash

os.chdir('c:\\MyScripts')

#this is how you can do a dry run. The deleting lines are commented out and the 
#variable is printed.

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)

send2trash.send2trash('.\\Hello.txt')