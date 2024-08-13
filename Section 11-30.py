'c:\\spam\\eggs.png'
print('\\')

import os
eggs = os.path.join('Folder1','Folder2','Folder3','file.png')
print(eggs)

print(os.getcwd())

print(os.path.abspath('Section 1-2.py'))


totalsize = 0
for filename in os.listdir('G:\\My Drive\\Learning\\Udemy\\Automate The Boring Stuff'):
    if not os.path.isfile(os.path.join('G:\\My Drive\\Learning\\Udemy\\Automate The Boring Stuff', filename)):
        continue
    totalsize = totalsize + os.path.getsize(os.path.join('G:\\My Drive\\Learning\\Udemy\\Automate The Boring Stuff', filename))

print(totalsize)