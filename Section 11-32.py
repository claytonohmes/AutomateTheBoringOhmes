import shutil
shutil.copy('Hello.txt', 'c:\\MyScripts\\HelloHello.txt')

shutil.copytree('c:\\MyScripts','c:\\MyScriptsBackup', dirs_exist_ok=True)