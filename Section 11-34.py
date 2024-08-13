import os
import shutil

for Foldername, subfolders, filenames in os.walk('c:\\MyScripts'):
    print('The folder is ' + Foldername)
    print('The sub folders in ' + Foldername + ' are: ' + str(subfolders))
    print('The filenames in ' + Foldername + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'chevy' in subfolder:
            os.rmdir(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(Foldername, file), os.join(Foldername, file + '.Backup'))
