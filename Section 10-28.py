import re
nameRegex = re.compile(r'Agent \w+')
print(nameRegex.findall('Agent Alice gave the secret message to Agent Bob.'))

print(nameRegex.sub('REDACTED','Agent Alice gave the secret message to Agent Bob.'))

nameRegex = re.compile(r'Agent (\w)\w*')
print(nameRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(nameRegex.sub(r'Agent \1*****', 'Agent Alice gave the secret documents to Agent Bob.'))

phoneNumbersRegex = re.compile('''
                               \d\d\d      #area code
                               -           #first dash
                               \d\d\d      #first 3 digits
                               -           #second dash
                               \d\d\d\d    #Last 4 digits''', re.VERBOSE)
